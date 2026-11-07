from pydantic import BaseModel, Field
from decimal import Decimal

class RestaurantSettingsBase(BaseModel):
    tax_rate: Decimal = Field(..., ge=0, le=100, decimal_places=2)
    currency_symbol: str = Field(..., min_length=1, max_length=10)
    currency_name: str = Field(..., min_length=1, max_length=50)

class RestaurantSettingsUpdate(BaseModel):
    tax_rate: Decimal | None = Field(None, ge=0, le=100, decimal_places=2)
    currency_symbol: str | None = Field(None, min_length=1, max_length=10)
    currency_name: str | None = Field(None, min_length=1, max_length=50)

class RestaurantSettingsResponse(RestaurantSettingsBase):
    id: int
    restaurant_id: int

    class Config:
        from_attributes = True
