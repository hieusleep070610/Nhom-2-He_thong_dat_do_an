from datetime import datetime, timezone
from fastapi.responses import JSONResponse


def create_response(
    status_code,
    message,
    data=None,
    error=None
):
    return JSONResponse(
        status_code=status_code,
        content={
            "status_code": status_code,
            "message": message,
            "data": data,
            "error": error,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    )