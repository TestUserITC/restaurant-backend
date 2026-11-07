from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.models.order import OrderStatus
from app.schemas.order import OrderCreate, OrderUpdate, OrderStatusUpdate, OrderResponse, OrderListResponse
from app.services import order as order_service

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("", response_model=list[OrderListResponse])
async def get_orders(
    status: OrderStatus | None = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=500),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get orders with optional status filtering (Owner & Cashier)"""
    orders = await order_service.get_orders(db, current_user.restaurant_id, status, skip, limit)
    
    # Enrich with item count
    result = []
    for order in orders:
        result.append({
            "id": order.id,
            "order_number": order.order_number,
            "status": order.status,
            "total": order.total,
            "item_count": len(order.items),
            "created_at": order.created_at
        })
    
    return result

@router.get("/stats", response_model=dict)
async def get_order_stats(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get order counts by status (Owner & Cashier)"""
    counts = await order_service.get_order_count_by_status(db, current_user.restaurant_id)
    return {
        "pending": counts[OrderStatus.PENDING],
        "in_preparation": counts[OrderStatus.IN_PREPARATION],
        "ready": counts[OrderStatus.READY]
    }

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(
    order_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get order detail (Owner & Cashier)"""
    return await order_service.get_order_detail(db, current_user.restaurant_id, order_id)

@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(
    order_data: OrderCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create a new order (Owner & Cashier)"""
    return await order_service.create_order(db, current_user.restaurant_id, order_data)

@router.patch("/{order_id}/status", response_model=OrderResponse)
async def update_order_status(
    order_id: int,
    status_update: OrderStatusUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update order status (Owner & Cashier)"""
    return await order_service.update_order_status(db, current_user.restaurant_id, order_id, status_update)

@router.patch("/{order_id}/notes", response_model=OrderResponse)
async def update_order_notes(
    order_id: int,
    order_data: OrderUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Update order notes (Owner & Cashier)"""
    return await order_service.update_order_notes(db, current_user.restaurant_id, order_id, order_data)
