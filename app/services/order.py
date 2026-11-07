from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_, func
from fastapi import HTTPException, status
from datetime import datetime, timezone
from decimal import Decimal
from app.models.order import Order, OrderItem, OrderStatus
from app.models.product import Product
from app.schemas.order import OrderCreate, OrderUpdate, OrderStatusUpdate

# State transition validations
STATE_TRANSITIONS = {
    OrderStatus.PENDING: [OrderStatus.IN_PREPARATION],
    OrderStatus.IN_PREPARATION: [OrderStatus.READY],
    OrderStatus.READY: [OrderStatus.CLOSED],
    OrderStatus.CLOSED: []  # No transitions from closed
}

async def get_orders(db: AsyncSession, restaurant_id: int, status: OrderStatus | None = None, skip: int = 0, limit: int = 50):
    """Get orders with optional status filtering"""
    query = select(Order).where(Order.restaurant_id == restaurant_id)
    
    if status:
        query = query.where(Order.status == status)
    
    query = query.order_by(Order.created_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def get_order_detail(db: AsyncSession, restaurant_id: int, order_id: int):
    """Get order detail with items"""
    result = await db.execute(
        select(Order).where(
            and_(
                Order.id == order_id,
                Order.restaurant_id == restaurant_id
            )
        )
    )
    
    order = result.scalars().first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Orden no encontrada"
        )
    
    return order

async def create_order(db: AsyncSession, restaurant_id: int, order_data: OrderCreate):
    """Create a new order with items"""
    # Import here to avoid circular imports
    from app.models.settings import RestaurantSettings
    from app.services.settings import get_or_create_settings
    
    # Generate order number
    latest_order = await db.execute(
        select(func.max(Order.id)).where(Order.restaurant_id == restaurant_id)
    )
    latest_id = latest_order.scalar() or 0
    order_number = f"#{latest_id + 1:04d}"
    
    # Get tax rate from settings
    restaurant_settings = await get_or_create_settings(db, restaurant_id)
    tax_rate = restaurant_settings.tax_rate
    
    # Calculate totals
    total_amount = Decimal("0")
    order_items = []
    
    for item_data in order_data.items:
        # Get product
        prod_result = await db.execute(
            select(Product).where(
                and_(
                    Product.id == item_data.product_id,
                    Product.restaurant_id == restaurant_id,
                    Product.deleted_at.is_(None)
                )
            )
        )
        product = prod_result.scalars().first()
        
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Producto {item_data.product_id} no encontrado"
            )
        
        subtotal = product.price * item_data.quantity
        total_amount += subtotal
        
        order_items.append({
            "product_id": product.id,
            "quantity": item_data.quantity,
            "unit_price": product.price,
            "subtotal": subtotal,
            "product_name": product.name
        })
    
    # Calculate tax
    tax_amount = (total_amount * tax_rate).quantize(Decimal("0.01"))
    final_total = total_amount + tax_amount
    
    # Create order
    order = Order(
        order_number=order_number,
        restaurant_id=restaurant_id,
        status=OrderStatus.PENDING,
        total=final_total,
        tax_amount=tax_amount,
        tax_rate=tax_rate,
        notes=order_data.notes
    )
    db.add(order)
    await db.flush()  # Get order ID
    
    # Add items
    for item_data in order_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item_data["product_id"],
            quantity=item_data["quantity"],
            unit_price=item_data["unit_price"],
            subtotal=item_data["subtotal"],
            product_name=item_data["product_name"]
        )
        db.add(order_item)
    
    await db.commit()
    await db.refresh(order)
    return order

async def update_order_status(db: AsyncSession, restaurant_id: int, order_id: int, status_update: OrderStatusUpdate):
    """Update order status with state machine validation"""
    order = await get_order_detail(db, restaurant_id, order_id)
    
    current_status = order.status
    new_status = status_update.status
    
    # Validate transition
    if new_status not in STATE_TRANSITIONS.get(current_status, []):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"No se puede cambiar de {current_status} a {new_status}"
        )
    
    order.status = new_status
    
    # Set closed_at if closing
    if new_status == OrderStatus.CLOSED:
        order.closed_at = datetime.now(timezone.utc)
    
    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order

async def update_order_notes(db: AsyncSession, restaurant_id: int, order_id: int, order_data: OrderUpdate):
    """Update order notes"""
    order = await get_order_detail(db, restaurant_id, order_id)
    
    order.notes = order_data.notes
    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order

async def get_order_count_by_status(db: AsyncSession, restaurant_id: int):
    """Get count of orders by status"""
    result = await db.execute(
        select(Order.status, func.count(Order.id))
        .where(Order.restaurant_id == restaurant_id)
        .where(Order.status != OrderStatus.CLOSED)
        .group_by(Order.status)
    )
    
    counts = {
        OrderStatus.PENDING: 0,
        OrderStatus.IN_PREPARATION: 0,
        OrderStatus.READY: 0
    }
    
    for status, count in result.all():
        counts[status] = count
    
    return counts

async def get_closed_orders(db: AsyncSession, restaurant_id: int, start_date: datetime | None = None, end_date: datetime | None = None, skip: int = 0, limit: int = 100):
    """Get closed orders (sales) with optional date range filtering"""
    query = select(Order).where(
        and_(
            Order.restaurant_id == restaurant_id,
            Order.status == OrderStatus.CLOSED
        )
    )
    
    if start_date:
        query = query.where(Order.closed_at >= start_date)
    
    if end_date:
        query = query.where(Order.closed_at <= end_date)
    
    query = query.order_by(Order.closed_at.desc()).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def get_sales_statistics(db: AsyncSession, restaurant_id: int, start_date: datetime | None = None, end_date: datetime | None = None):
    """Get sales statistics for a date range"""
    query = select(
        func.count(Order.id).label("total_sales"),
        func.sum(Order.total).label("total_revenue"),
        func.avg(Order.total).label("average_sale")
    ).where(
        and_(
            Order.restaurant_id == restaurant_id,
            Order.status == OrderStatus.CLOSED
        )
    )
    
    if start_date:
        query = query.where(Order.closed_at >= start_date)
    
    if end_date:
        query = query.where(Order.closed_at <= end_date)
    
    result = await db.execute(query)
    row = result.first()
    
    return {
        "total_sales": row[0] or 0,
        "total_revenue": row[1] or Decimal("0"),
        "average_sale": row[2] or Decimal("0")
    }
