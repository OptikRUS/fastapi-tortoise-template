from pydantic import BaseModel

from common.orm import BaseRepo


class BaseAuthorModel(BaseModel):
    """
    Базовая модель автора
    """


class BaseAuthorRepo(BaseRepo):
    """
    Базовый репозиторий автора
    """


class BaseGenreModel(BaseModel):
    """
    Базовая модель жанра
    """


class BaseGenreRepo(BaseRepo):
    """
    Базовый репозиторий жанра
    """


class BaseBookModel(BaseModel):
    """
    Базовая модель книги
    """


class BaseBookRepo(BaseRepo):
    """
    Базовый репозиторий книги
    """
