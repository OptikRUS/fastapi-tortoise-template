from fastapi import APIRouter, Depends

from users.security import get_current_admin, get_current_user
from users.models import User
from library import schemas
from library.use_cases import (
    GenreCreationCase, GetGenresCase, AuthorCreationCase, GetAuthorsCase, BookCreationCase, GetBooksCase, GetBookCase
)


library_router = APIRouter(prefix="/library", tags=["library"])


@library_router.post("/add_genre", status_code=201, response_model=schemas.GenreResponse)
async def create_genre_by_admin(genre: schemas.CreateGenre, current_admin: User = Depends(get_current_admin)):
    """
    Добавление жанра книги админом
    """

    genre_creation: GenreCreationCase = GenreCreationCase()
    return await genre_creation(genre)


@library_router.get("/all_genres", status_code=200, response_model=list[schemas.GenreResponse])
async def get_all_genres(current_user: User = Depends(get_current_user)):
    """
    Список всех жанров
    """

    all_users = GetGenresCase()
    return await all_users()


@library_router.post("/add_author", status_code=201, response_model=schemas.AuthorResponse)
async def create_author_by_admin(author: schemas.CreateAuthor, current_admin: User = Depends(get_current_admin)):
    """
    Добавление автора книги админом
    """

    author_creation: AuthorCreationCase = AuthorCreationCase()
    return await author_creation(author)


@library_router.get("/all_authors", status_code=200, response_model=list[schemas.AuthorResponse])
async def get_all_authors(current_user: User = Depends(get_current_user)):
    """
    Список всех авторов
    """

    all_authors = GetAuthorsCase()
    return await all_authors()


@library_router.post("/create_book", status_code=201, response_model=schemas.BookResponse)
async def register_book_for_admin(book: schemas.CreateBook, current_admin: User = Depends(get_current_admin)):
    """
    Регистрации книги админом
    """

    book_creation: BookCreationCase = BookCreationCase()
    return await book_creation(book)


@library_router.get("/all_books", status_code=200, response_model=list[schemas.BookResponse])
async def get_all_books(current_user: User = Depends(get_current_user)):
    """
    Список всех книг
    """

    all_books = GetBooksCase()
    return await all_books()


@library_router.get("/{book_id}", status_code=200, response_model=schemas.BookResponse)
async def get_book_info(book_id: int, current_user: User = Depends(get_current_user)):
    """
    Получение информации о книге
    """

    get_book = GetBookCase()
    return await get_book(book_id)
