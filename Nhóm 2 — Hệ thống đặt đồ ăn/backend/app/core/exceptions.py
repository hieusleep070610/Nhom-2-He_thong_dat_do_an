from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
from app.core.response import create_response


async def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    return create_response(
        exc.status_code,
        "Có lỗi xảy ra",
        error=str(exc.detail)
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return create_response(
        422,
        "Dữ liệu đầu vào không hợp lệ",
        error=exc.errors()
    )


async def general_exception_handler(
    request: Request,
    exc: Exception
):
    return create_response(
        500,
        "Lỗi hệ thống",
        error="Đã xảy ra lỗi không mong muốn"
    )