"""Điểm khởi động của backend.

Chạy:  uvicorn app.main:app --reload
Tài liệu API tự sinh: http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "He thong dat do an dang hoat dong!"
    }

