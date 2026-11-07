from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_, func
from datetime import datetime, timezone, timedelta
from decimal import Decimal
from app.models.order import Order, OrderStatus
from app.models.product import Product

async def get_owner_dashboard(db: AsyncSession, restaurant_id: int):
    """Get comprehensive dashboard data for Owner"""
    today_start = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start + timedelta(days=1)
    
    # Total sales today
    today_sales = await db.execute(
        select(func.count(Order.id), func.sum(Order.total))
        .where(
            and_(
                Order.restaurant_id == restaurant_id,
                Order.status == OrderStatus.CLOSED,
                Order.closed_at >= today_start,
                Order.closed_at < today_end
            )
        )
    )
    today_count, today_total = today_sales.first()
    
    # Open orders
    open_orders = await db.execute(
        select(func.count(Order.id))
        .where(
            and_(
                Order.restaurant_id == restaurant_id,
                Order.status.in_([OrderStatus.PENDING, OrderStatus.IN_PREPARATION, OrderStatus.READY])
            )
        )
    )
    open_count = open_orders.scalar() or 0
    
    # Average ticket today
    avg_ticket = (today_total / today_count if today_count and today_count > 0 else Decimal("0"))
    
    # Top products today
    top_products = await db.execute(
        select(
            Product.name,
            func.sum(Product.price * func.count()).label("revenue"),
            func.sum(func.count()).label("qty")
        )
        .select_from(Product)
        .join(Order)
        .where(
            and_(
                Order.restaurant_id == restaurant_id,
                Order.status == OrderStatus.CLOSED,
                Order.closed_at >= today_start,
                Order.closed_at < today_end
            )
        )
        .group_by(Product.id, Product.name)
        .order_by(func.sum(func.count()).desc())
        .limit(5)
    )
    
    return {
        "today_sales": today_count or 0,
        "today_revenue": float(today_total or 0),
        "average_ticket": float(avg_ticket),
        "open_orders": open_count,
        "top_products": [{"name": name, "qty": qty or 0} for name, revenue, qty in top_products.all()]
    }

async def get_cashier_dashboard(db: AsyncSession, restaurant_id: int):
    """Get operational dashboard data for Cashier (limited)"""
    # Open orders
    open_orders_result = await db.execute(
        select(func.count(Order.id).label("pending"), 
               func.count().filter(Order.status == OrderStatus.IN_PREPARATION).label("prep"),
               func.count().filter(Order.status == OrderStatus.READY).label("ready"))
        .where(
            and_(
                Order.restaurant_id == restaurant_id,
                Order.status.in_([OrderStatus.PENDING, OrderStatus.IN_PREPARATION, OrderStatus.READY])
            )
        )
    )
    
    result = open_orders_result.first()
    
    return {
        "pending_orders": result[0] or 0,
        "in_preparation": result[1] or 0,
        "ready_orders": result[2] or 0
    }
