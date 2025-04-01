from typing import List

from pydantic import BaseModel

class OrderItem(BaseModel):
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    user_id: int
    items: List[OrderItem]

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_price: float
    items: List[OrderItem]
    status: str
