from http.client import HTTPException

from fastapi import APIRouter, status

from src.digital_store.schemas.order import OrderResponse, OrderCreate

router = APIRouter(
    tags=["orders"],
)

@router.post("/orders", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(order_data: OrderCreate):
    # вычисляем total_price (пока без реальной логики)
    total_price = 0
    for item in order_data.items:
        total_price += (item.quantity * 100)

    new_order = {
        "id": 1,
        "user_id": order_data.user_id,
        "total_price": total_price,
        "items": order_data.items,
        "status": "new"
    }
    return new_order

@router.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(order_id: int):
    if order_id == 1:
        return {
            "id": 1,
            "user_id": 1,
            "total_price": 300,
            "items": [
                {"product_id": 10, "quantity": 3},
            ],
            "status": "new"
        }
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND)