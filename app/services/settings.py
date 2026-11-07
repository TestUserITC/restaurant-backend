from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models.settings import RestaurantSettings
from app.schemas.settings import RestaurantSettingsUpdate

async def get_or_create_settings(db: AsyncSession, restaurant_id: int):
    """Get settings or create defaults for a restaurant"""
    result = await db.execute(
        select(RestaurantSettings).where(
            RestaurantSettings.restaurant_id == restaurant_id
        )
    )
    
    settings = result.scalars().first()
    if not settings:
        # Create default settings
        settings = RestaurantSettings(
            restaurant_id=restaurant_id,
            tax_rate="0.18",
            currency_symbol="$",
            currency_name="USD"
        )
        db.add(settings)
        await db.commit()
        await db.refresh(settings)
    
    return settings

async def update_settings(db: AsyncSession, restaurant_id: int, settings_data: RestaurantSettingsUpdate):
    """Update restaurant settings"""
    settings = await get_or_create_settings(db, restaurant_id)
    
    if settings_data.tax_rate is not None:
        settings.tax_rate = settings_data.tax_rate
    
    if settings_data.currency_symbol is not None:
        settings.currency_symbol = settings_data.currency_symbol
    
    if settings_data.currency_name is not None:
        settings.currency_name = settings_data.currency_name
    
    db.add(settings)
    await db.commit()
    await db.refresh(settings)
    return settings
