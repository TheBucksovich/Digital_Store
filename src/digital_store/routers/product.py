from fastapi import APIRouter, status, HTTPException

from src.digital_store.schemas.product import ProductResponse, ProductCreate

router = APIRouter(
    tags=["products"],
)

@router.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductCreate):
    new_product = {
        "id": 1,
        "name": product_data.name,
        "price": product_data.price,
        "in_stock": product_data.in_stock,
    }
    return new_product

@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    if product_id == 1:
        return {
            "id": 1,
            "name": "Laptop",
            "price": 999.99,
            "in_stock": True,
        }
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND)