from fastapi import APIRouter, Depends, Query

from common.security import UserAuth, UserType
from src.users.repos import User
from ..use_cases import AuthorCreationCase, GetAuthorCase
from ..models import CreateAuthorRequest, AuthorResponse
from ..exceptions.models import BaseAuthorExceptionModel

router = APIRouter(prefix="/authors", tags=["authors"])


@router.post(
    "/create",
    status_code=201,
    response_model=AuthorResponse,
    responses={409: {"model": BaseAuthorExceptionModel}}
)
async def create_author_by_admin(author: CreateAuthorRequest, auth: User = Depends(UserAuth(UserType.ADMIN))):
    """
    Добавление автора книги админом
    """

    author_creation: AuthorCreationCase = AuthorCreationCase()
    return await author_creation(author)


@router.get(
    "/get",
    status_code=200,
    response_model=list[AuthorResponse],
    responses={404: {"model": BaseAuthorExceptionModel}}
)
async def get_authors(author_id: int = Query(None), auth: User = Depends(UserAuth(UserType.ANY))):
    """
    Получение автора по id или всех авторов
    """

    author = GetAuthorCase()
    return await author(author_id)
