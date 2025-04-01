from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    in_stock: bool

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool
