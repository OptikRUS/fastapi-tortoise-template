from fastapi import APIRouter, Depends, Query

from users.security import UserAuth, UserType
from users.models import User
from library import schemas, use_cases as library_cases


library_router = APIRouter(prefix="/library", tags=["library"])


@library_router.post("/create_genre", status_code=201, response_model=schemas.GenreResponse)
async def create_genre_by_admin(genre: schemas.CreateGenre, current_admin: User = Depends(UserAuth(UserType.ADMIN))):
    """
    Добавление жанра книги админом
    """

    genre_creation: library_cases.GenreCreationCase = library_cases.GenreCreationCase()
    return await genre_creation(genre)


@library_router.get("/genres/", status_code=200, response_model=list[schemas.GenreResponse])
async def get_genres(genre_id: int = Query(None), current_user: User = Depends(UserAuth(UserType.ANY))):
    """
    Получение жанра по id или всех жанров
    """

    genres = library_cases.GetGenresCase()
    return await genres(genre_id)


@library_router.post("/create_author", status_code=201, response_model=schemas.AuthorResponse)
async def create_author_by_admin(author: schemas.CreateAuthor, current_admin: User = Depends(UserAuth(UserType.ADMIN))):
    """
    Добавление автора книги админом
    """

    author_creation: library_cases.AuthorCreationCase = library_cases.AuthorCreationCase()
    return await author_creation(author)


@library_router.get("/authors", status_code=200, response_model=list[schemas.AuthorResponse])
async def get_authors(author_id: int = Query(None), current_user: User = Depends(UserAuth(UserType.ANY))):
    """
    Получение автора по id или всех авторов
    """

    author = library_cases.GetAuthorCase()
    return await author(author_id)


@library_router.post("/create_book", status_code=201, response_model=schemas.BookDetailResponse)
async def register_book_for_admin(book: schemas.CreateBook, current_admin: User = Depends(UserAuth(UserType.ADMIN))):
    """
    Регистрации книги админом
    """

    book_creation: library_cases.BookCreationCase = library_cases.BookCreationCase()
    return await book_creation(book)


@library_router.get("/books", status_code=200, response_model=list[schemas.BookResponse])
async def get_books(book_id: int = Query(None), current_user: User = Depends(UserAuth(UserType.ANY))):
    """
    Получение книги по id или всех книг
    """

    books = library_cases.GetBooksCase()
    return await books(book_id)


@library_router.get("/books/{book_id}", status_code=200, response_model=schemas.BookDetailResponse)
async def get_book_detail(book_id: int, current_user: User = Depends(UserAuth(UserType.ANY))):
    """
    Получение информации книги по id
    """

    books = library_cases.GetBookDetailCase()
    return await books(book_id)


@library_router.get("/search_book", status_code=200, response_model=schemas.BooksResponse)
async def get_search_book(search_book: str = Query(None), current_user: User = Depends(UserAuth(UserType.ANY))):
    """
    Поиск книг по названию или описанию
    """

    get_book = library_cases.SearchBookCase()
    return await get_book(search_book)
