"""Kiểm tra server và kết nối DB còn sống không: GET /api/health"""

from fastapi import APIRouter
from sqlalchemy import text
from app.db.session import engine

router_health = APIRouter(tags=["Health"])

@router_health.get("/api/health")
def health():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"status": "ok", "db": "connected"}