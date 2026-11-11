"""Kết nối MySQL bằng SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://root:cellfite90@localhost:3306/foodpay"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Hàm cung cấp session database cho các request API"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()