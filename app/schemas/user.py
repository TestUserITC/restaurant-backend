from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from app.models.user import UserRole

class UserBase(BaseModel):
    email: EmailStr
    full_name: str = Field(..., min_length=3, max_length=100)
    role: UserRole = UserRole.CASHIER

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserResponse(UserBase):
    id: int
    restaurant_id: int | None
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
