from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime

class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    price: Decimal = Field(..., gt=0, max_digits=10, decimal_places=2)
    category_id: int
    description: str | None = Field(None, max_length=500)
    image_url: str | None = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    price: Decimal = Field(..., gt=0, max_digits=10, decimal_places=2)
    category_id: int
    description: str | None = Field(None, max_length=500)
    image_url: str | None = None

class ProductResponse(ProductBase):
    id: int
    is_available: bool
    created_at: datetime

    class Config:
        from_attributes = True

class ProductListResponse(BaseModel):
    id: int
    name: str
    price: Decimal
    category_id: int
    category_name: str
    is_available: bool
    image_url: str | None
    created_at: datetime

    class Config:
        from_attributes = True
