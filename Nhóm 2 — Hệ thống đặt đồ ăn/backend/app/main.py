from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    general_exception_handler
)

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

app = FastAPI(title="QuickBite API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    Exception,
    general_exception_handler
)


@app.get("/")
def healthy():
    return {
        "message": "QuickBite API is running"
    }