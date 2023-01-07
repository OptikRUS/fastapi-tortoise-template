from pydantic import BaseModel

from common.orm import BaseRepo
from common.exceptions import BaseExceptionModel


class BaseUserModel(BaseModel):
    """
    Базовая модель пользователя
    """


class BaseUserRepo(BaseRepo):
    """
    Базовый репозиторий пользователя
    """


class BaseUserExceptionModel(BaseExceptionModel):
    """
    Базовый репозиторий пользователя
    """
