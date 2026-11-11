"""Điểm khởi động của backend.

Chạy:  uvicorn app.main:app --reload
Tài liệu API tự sinh: http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.wallet import router_wallet
from app.routers.health import router_health

app = FastAPI(title="FoodPay API")

# Cấu hình CORS để cho phép Frontend (Live Server, React,...) gọi API không bị chặn
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả các nguồn gọi vào
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép mọi phương thức (GET, POST, PUT, DELETE...)
    allow_headers=["*"],  # Cho phép mọi header
)

app.include_router(router_wallet)
app.include_router(router_health)

@app.get("/")
def home():
    return {
        "message": "Api đang chạy"
    }