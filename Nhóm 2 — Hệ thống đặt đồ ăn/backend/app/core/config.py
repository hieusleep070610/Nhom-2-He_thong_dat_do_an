"""Đọc cấu hình từ file .env (hoặc biến môi trường).

Muốn thêm cấu hình mới: thêm 1 dòng vào class Settings + thêm vào .env.example.
"""
import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM_DB: str = os.getenv("ALGORITHM_DB")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 5
    DB_PASS: str = os.getenv("DB_PASSWORD")
    DATABASE_URL: str = f"mysql+pymysql://root:{DB_PASS}@localhost:3306/project_db"

settings = Settings()