from common.exceptions import BaseBadRequestError, BaseNotFoundError, BaseConflictError


"""
Ошибки библиотеки
"""


class AuthorFullNameError(BaseBadRequestError):
    message: str = "Отсутствует ФИО автора."
    reason: str = "author_full_name_error"


class GenreNotFoundError(BaseNotFoundError):
    message: str = "Жанр не найден."
    reason: str = "genre_not_found"


class GenresNotFoundError(BaseNotFoundError):
    message: str = "Жанры не найдены."
    reason: str = "genres_not_found"


class AuthorNotFoundError(BaseNotFoundError):
    message: str = "Автор не найден."
    reason: str = "author_not_found"


class AuthorsNotFoundError(BaseNotFoundError):
    message: str = "Авторы не найдены."
    reason: str = "authors_not_found"


class GenreAlreadyExistError(BaseConflictError):
    message: str = "Такой жанр уже существует."
    reason: str = "genre_already_exist"


class AuthorAlreadyExistError(BaseConflictError):
    message: str = "Такой автор уже существует."
    reason: str = "author_already_exist"


class BookNotFoundError(BaseNotFoundError):
    message: str = "Книга не найдена."
    reason: str = "book_not_found"


class BooksNotFoundError(BaseNotFoundError):
    message: str = "Книги не найдены."
    reason: str = "books_not_found"


class BookAlreadyExistError(BaseConflictError):
    message: str = "Книга с таким названием уже существует."
    reason: str = "book_already_exist"
