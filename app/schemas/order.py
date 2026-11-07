from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime
from app.models.order import OrderStatus

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., ge=1)

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    product_name: str
    quantity: int
    unit_price: Decimal
    subtotal: Decimal

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    items: list[OrderItemCreate]
    notes: str | None = None

class OrderUpdate(BaseModel):
    notes: str | None = None

class OrderStatusUpdate(BaseModel):
    status: OrderStatus

class OrderResponse(BaseModel):
    id: int
    order_number: str
    status: OrderStatus
    total: Decimal
    tax_amount: Decimal
    tax_rate: Decimal
    notes: str | None
    items: list[OrderItemResponse]
    created_at: datetime
    closed_at: datetime | None

    class Config:
        from_attributes = True

class OrderListResponse(BaseModel):
    id: int
    order_number: str
    status: OrderStatus
    total: Decimal
    item_count: int
    created_at: datetime

    class Config:
        from_attributes = True
