from pydantic import BaseModel, Field


class BaseExceptionModel(BaseModel):
    message: str = Field("Сообщение об ошибке.")
    reason: str = Field("error_reason")
    ok: bool = Field(False)
