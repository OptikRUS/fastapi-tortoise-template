from typing import Any, Optional

from fastapi import HTTPException


class BaseLibraryException(HTTPException):
    """
    Базовая HTTP-ошибка автора
    """
    status: int
    message: Any = None
    headers: Optional[dict[str, Any]] = None

    def __init__(self) -> None:
        super().__init__(status_code=self.status, detail=self.message, headers=self.headers)
