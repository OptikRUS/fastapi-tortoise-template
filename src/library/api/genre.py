from fastapi import APIRouter, Depends, Query

from common.security import UserAuth, UserType
from src.users.repos import User
from ..use_cases import GenreCreationCase, GetGenresCase
from ..models import GenreResponse, CreateGenre
from ..exceptions.models import BaseGenreExceptionModel

router = APIRouter(prefix="/genres", tags=["genres"])


@router.post(
    "/create",
    status_code=201,
    response_model=GenreResponse,
    responses={409: {"model": BaseGenreExceptionModel}}
)
async def create_genre_by_admin(genre: CreateGenre, auth: User = Depends(UserAuth(UserType.ADMIN))):
    """
    Добавление жанра книги админом
    """

    genre_creation: GenreCreationCase = GenreCreationCase()
    return await genre_creation(genre)


@router.get(
    "/get",
    status_code=200,
    response_model=list[GenreResponse],
    responses={404: {"model": BaseGenreExceptionModel}}
)
async def get_genres(genre_id: int = Query(None), auth: User = Depends(UserAuth(UserType.ANY))):
    """
    Получение жанра по id или всех жанров
    """

    genres = GetGenresCase()
    return await genres(genre_id)
