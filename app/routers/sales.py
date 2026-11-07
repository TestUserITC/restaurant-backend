from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone, timedelta
from app.dependencies import get_db, get_current_active_owner
from app.models.user import User
from app.schemas.order import OrderListResponse
from app.services import order as order_service

router = APIRouter(prefix="/sales", tags=["Sales & Reporting"])

@router.get("/history", response_model=list[OrderListResponse])
async def get_sales_history(
    start_date: datetime | None = Query(None, description="Filter from date (ISO format)"),
    end_date: datetime | None = Query(None, description="Filter to date (ISO format)"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Get sales history with optional date range (Owner only)"""
    orders = await order_service.get_closed_orders(db, current_user.restaurant_id, start_date, end_date, skip, limit)
    
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

@router.get("/statistics", response_model=dict)
async def get_sales_stats(
    start_date: datetime | None = Query(None, description="Filter from date (ISO format)"),
    end_date: datetime | None = Query(None, description="Filter to date (ISO format)"),
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Get sales statistics for a date range (Owner only)"""
    stats = await order_service.get_sales_statistics(db, current_user.restaurant_id, start_date, end_date)
    return {
        "total_sales": stats["total_sales"],
        "total_revenue": float(stats["total_revenue"]),
        "average_sale": float(stats["average_sale"])
    }

@router.get("/today", response_model=dict)
async def get_today_sales(
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Get today's sales summary (Owner only)"""
    today_start = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start + timedelta(days=1)
    
    stats = await order_service.get_sales_statistics(db, current_user.restaurant_id, today_start, today_end)
    return {
        "date": today_start.date(),
        "total_sales": stats["total_sales"],
        "total_revenue": float(stats["total_revenue"]),
        "average_sale": float(stats["average_sale"])
    }
