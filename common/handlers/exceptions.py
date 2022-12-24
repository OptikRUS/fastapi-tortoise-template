from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse


def common_exception_handler(request: Request, exception: Exception) -> JSONResponse:
    """
    Общий обработчик исключений
    """

    status_code = getattr(exception, "status", status.HTTP_400_BAD_REQUEST)
    content = {
        "message": getattr(exception, "message", "Ошибка."),
        "reason": getattr(exception, "reason", "error"),
        "ok": getattr(exception, "ok", False)
    }

    return JSONResponse(status_code=status_code, content=content)
