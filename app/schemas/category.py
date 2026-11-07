from pydantic import BaseModel, Field
from datetime import datetime

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)

class CategoryResponse(CategoryBase):
    id: int
    is_active: bool
    created_at: datetime
    product_count: int = 0

    class Config:
        from_attributes = True

class CategoryListResponse(BaseModel):
    id: int
    name: str
    is_active: bool
    product_count: int
    created_at: datetime

    class Config:
        from_attributes = True
