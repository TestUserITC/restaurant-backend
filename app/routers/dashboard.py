from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db, get_current_user
from app.models.user import User, UserRole
from app.services import dashboard as dashboard_service

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/owner", response_model=dict)
async def get_owner_dashboard(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get owner dashboard (comprehensive KPIs) - Owner only"""
    if current_user.role != UserRole.OWNER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Owner role required")
    
    return await dashboard_service.get_owner_dashboard(db, current_user.restaurant_id)

@router.get("/cashier", response_model=dict)
async def get_cashier_dashboard(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get cashier dashboard (operational KPIs) - Owner & Cashier"""
    return await dashboard_service.get_cashier_dashboard(db, current_user.restaurant_id)
