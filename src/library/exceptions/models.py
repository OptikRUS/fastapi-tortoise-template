from common.exceptions.models import BaseExceptionModel


class BaseAuthorExceptionModel(BaseExceptionModel):
    """
    Базовая модель ошибки автора
    """


class BaseBookExceptionModel(BaseExceptionModel):
    """
    Базовая модель ошибки книги
    """


class BaseGenreExceptionModel(BaseExceptionModel):
    """
    Базовая модель ошибки жанра
    """
