from common.exceptions.models import BaseExceptionModel


class BaseAuthorExceptionModel(BaseExceptionModel):
    """
    Базовый репозиторий автора
    """


class BaseBookExceptionModel(BaseExceptionModel):
    """
    Базовый репозиторий книги
    """


class BaseGenreExceptionModel(BaseExceptionModel):
    """
    Базовый репозиторий жанра
    """
