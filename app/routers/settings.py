from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db, get_current_active_owner
from app.models.user import User
from app.schemas.settings import RestaurantSettingsResponse, RestaurantSettingsUpdate
from app.services import settings as settings_service

router = APIRouter(prefix="/settings", tags=["Settings"])

@router.get("", response_model=RestaurantSettingsResponse)
async def get_settings(
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Get restaurant settings (Owner only)"""
    return await settings_service.get_or_create_settings(db, current_user.restaurant_id)

@router.patch("", response_model=RestaurantSettingsResponse)
async def update_settings(
    settings_data: RestaurantSettingsUpdate,
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Update restaurant settings (Owner only)"""
    return await settings_service.update_settings(db, current_user.restaurant_id, settings_data)
