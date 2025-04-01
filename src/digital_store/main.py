from fastapi import FastAPI
from src.digital_store.routers.user import router as user_router
from src.digital_store.routers.product import router as product_router
from src.digital_store.routers.order import router as order_router


app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)