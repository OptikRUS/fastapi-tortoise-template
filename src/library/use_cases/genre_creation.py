from ..models import CreateGenre
from ..repos import GenreRepo, Genre
from ..exceptions import GenreAlreadyExistError


class GenreCreationCase:
    """
    Кейс создания жанра
    """

    def __init__(self) -> None:
        self.genre_repo: GenreRepo = GenreRepo()

    async def __call__(self, genre: CreateGenre) -> Genre:
        genre_filters: dict = dict(name__iexact=genre.name)
        genre_exist: bool = await self.genre_repo.exists(filters=genre_filters)

        if genre_exist:
            raise GenreAlreadyExistError
        new_genre: Genre = await Genre.create(**genre.dict())
        return new_genre
