from fastapi import APIRouter, Depends

from users.security import get_current_admin, get_current_user
from users.models import User
from library import schemas, use_cases as library_cases


library_router = APIRouter(prefix="/library", tags=["library"])


@library_router.post("/create_genre", status_code=201, response_model=schemas.GenreResponse)
async def create_genre_by_admin(genre: schemas.CreateGenre, current_admin: User = Depends(get_current_admin)):
    """
    Добавление жанра книги админом
    """

    genre_creation: library_cases.GenreCreationCase = library_cases.GenreCreationCase()
    return await genre_creation(genre)


@library_router.get("/all_genres", status_code=200, response_model=list[schemas.GenreResponse])
async def get_all_genres(current_user: User = Depends(get_current_user)):
    """
    Список всех жанров
    """

    all_users = library_cases.GetGenresCase()
    return await all_users()


@library_router.post("/create_author", status_code=201, response_model=schemas.AuthorResponse)
async def create_author_by_admin(author: schemas.CreateAuthor, current_admin: User = Depends(get_current_admin)):
    """
    Добавление автора книги админом
    """

    author_creation: library_cases.AuthorCreationCase = library_cases.AuthorCreationCase()
    return await author_creation(author)


@library_router.get("/all_authors", status_code=200, response_model=list[schemas.AuthorResponse])
async def get_all_authors(current_user: User = Depends(get_current_user)):
    """
    Список всех авторов
    """

    all_authors = library_cases.GetAuthorsCase()
    return await all_authors()


@library_router.post("/create_book", status_code=201, response_model=schemas.BookResponse)
async def register_book_for_admin(book: schemas.CreateBook, current_admin: User = Depends(get_current_admin)):
    """
    Регистрации книги админом
    """

    book_creation: library_cases.BookCreationCase = library_cases.BookCreationCase()
    return await book_creation(book)


@library_router.get("/all_books", status_code=200, response_model=list[schemas.BookResponse])
async def get_all_books(current_user: User = Depends(get_current_user)):
    """
    Список всех книг
    """

    all_books = library_cases.GetBooksCase()
    return await all_books()


@library_router.get("/{book_id}", status_code=200, response_model=schemas.BookResponse)
async def get_book_info(book_id: int, current_user: User = Depends(get_current_user)):
    """
    Получение информации о книге
    """

    get_book = library_cases.GetBookCase()
    return await get_book(book_id)
