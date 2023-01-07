from fastapi import APIRouter, Depends, Query

from common.security import UserAuth, UserType
from src.users.repos import User
from ..use_cases import BookCreationCase, GetBooksCase, GetBookDetailCase, SearchBookCase
from ..models import BookDetailResponse, CreateBookRequest, BookResponse, BooksResponse
from ..exceptions.models import BaseBookExceptionModel

router = APIRouter(prefix="/books", tags=["books"])


@router.post(
    "/create",
    status_code=201,
    response_model=BookDetailResponse,
    responses={
        409: {"model": BaseBookExceptionModel},
        404: {"model": BaseBookExceptionModel}
    }
)
async def register_book_for_admin(book_data: CreateBookRequest, auth: User = Depends(UserAuth(UserType.ADMIN))):
    """
    Регистрации книги админом
    """

    book_creation: BookCreationCase = BookCreationCase()
    return await book_creation(book_data)


@router.get(
    "/get",
    status_code=200,
    response_model=list[BookResponse],
    responses={
        404: {"model": BaseBookExceptionModel}
    }
)
async def get_books(book_id: int = Query(None), auth: User = Depends(UserAuth(UserType.ANY))):
    """
    Получение книги по id или всех книг
    """

    books: GetBooksCase = GetBooksCase()
    return await books(book_id)


@router.get(
    "/{book_id}",
    status_code=200,
    response_model=BookDetailResponse,
    responses={
        404: {"model": BaseBookExceptionModel}
    }
)
async def get_book_detail(book_id: int, auth: User = Depends(UserAuth(UserType.ANY))):
    """
    Получение информации книги по id
    """

    book: GetBookDetailCase = GetBookDetailCase()
    return await book(book_id)


@router.get(
    "/",
    status_code=200,
    response_model=BooksResponse,
    responses={
        404: {"model": BaseBookExceptionModel}
    }
)
async def get_search_book(search_book: str = Query(None), auth: User = Depends(UserAuth(UserType.ANY))):
    """
    Поиск книг по названию или описанию
    """
    books: SearchBookCase = SearchBookCase()
    return await books(search_book)
