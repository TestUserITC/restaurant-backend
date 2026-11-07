from pydantic import BaseModel, Field, EmailStr, model_validator, field_validator
from app.schemas.user import UserCreate

class RestaurantBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    address: str | None = Field(None, max_length=200)

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantResponse(RestaurantBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

class RegisterRequest(BaseModel):
    restaurant_name: str = Field(..., min_length=3, max_length=100)
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)
    confirm_password: str
    address: str | None = Field(None, max_length=200)
    accept_terms: bool = Field(..., description="Must accept terms and conditions")

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if not any(c.isalpha() for c in v) or not any(c.isdigit() for c in v):
            raise ValueError('La contraseña debe contener al menos una letra y un número')
        return v

    @model_validator(mode="after")
    def check_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Las contraseñas no coinciden")
        return self
