from tortoise.functions import Lower

from .schemas import CreateGenre
from .models import Genres
from .exceptions import GenreAlreadyExistError, GenresNotFoundError


class GenreCreationCase:
    """
    Кейс создания жанра
    """

    async def __call__(self, genre: CreateGenre):
        genre_exist = await Genres.exists(name__iexact=genre.name)

        if genre_exist:
            raise GenreAlreadyExistError
        new_genre = await Genres.create(**genre.dict())
        return new_genre


class GetAllGenres:
    """
    Кейс получения всех жанров
    """

    async def __call__(self):
        all_genres = await Genres.all()
        if all_genres:
            return all_genres
        raise GenresNotFoundError
