from pydantic import BaseModel, Field, field_validator
from decimal import Decimal

class RestaurantSettingsBase(BaseModel):
    tax_rate: Decimal = Field(..., ge=0, le=100, decimal_places=2)
    currency_symbol: str = Field(..., min_length=1, max_length=10)
    currency_name: str = Field(..., min_length=1, max_length=50)

class RestaurantSettingsUpdate(BaseModel):
    tax_rate: Decimal | None = Field(None, ge=0, le=1, decimal_places=2)
    currency_symbol: str | None = Field(None, min_length=1, max_length=10)
    currency_name: str | None = Field(None, min_length=1, max_length=50)

    @field_validator('tax_rate', mode='before')
    def validate_tax_rate_fraction(cls, v):
        if v is None:
            return v
        if isinstance(v, str):
            v = v.strip()
            if v == "":
                raise ValueError("tax_rate must be between 0 and 1 inclusive")
        try:
            dec = Decimal(v)
        except Exception:
            raise ValueError("tax_rate must be between 0 and 1 inclusive")
        if dec < 0 or dec > 1:
            raise ValueError("tax_rate must be between 0 and 1 inclusive")
        return dec

class RestaurantSettingsResponse(RestaurantSettingsBase):
    id: int
    restaurant_id: int

    class Config:
        from_attributes = True
