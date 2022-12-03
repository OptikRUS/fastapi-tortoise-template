from fastapi import APIRouter, Depends

from library import schemas
from users.security import get_current_admin, get_current_user
from users.models import Users


library_router = APIRouter(prefix="/library", tags=["library"])


@library_router.post("/add_genre", status_code=201, response_model=schemas.GenreResponse)
async def create_genre_by_admin(genre: schemas.CreateGenre, current_admin: Users = Depends(get_current_admin)):
    """
    Добавление жанра книги админом
    """

    return None


@library_router.get("/all_genres", status_code=200, response_model=list[schemas.GenreResponse])
async def get_all_genres(current_user: Users = Depends(get_current_user)):
    """
    Список всех жанров
    """

    return None


@library_router.post("/add_author", status_code=201, response_model=schemas.AuthorResponse)
async def create_author_by_admin(author: schemas.CreateAuthor, current_admin: Users = Depends(get_current_admin)):
    """
    Добавление автора книги админом
    """

    return None


@library_router.get("/all_authors", status_code=200, response_model=list[schemas.AuthorResponse])
async def get_all_authors(current_user: Users = Depends(get_current_user)):
    """
    Список всех авторов
    """

    return None


@library_router.post("/create_book", status_code=201, response_model=schemas.BookResponse)
async def register_book_for_admin(book: schemas.CreateBook, current_admin: Users = Depends(get_current_admin)):
    """
    Регистрации книги админом
    """

    return None


@library_router.get("/all_books", status_code=200, response_model=list[schemas.BookResponse])
async def get_all_books(current_user: Users = Depends(get_current_user)):
    """
    Список всех книг
    """

    return None
