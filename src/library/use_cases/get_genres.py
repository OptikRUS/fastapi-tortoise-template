from ..repos import GenreRepo, Genre
from ..exceptions import GenresNotFoundError


class GetGenresCase:
    """
    Кейс получения жанра(ов)
    """

    def __init__(self) -> None:
        self.genre_repo: GenreRepo = GenreRepo()

    async def __call__(self, genre_id: int = None) -> list[Genre]:
        filters: dict = dict()

        if genre_id:
            filters = dict(id=genre_id)
        genres: list[Genre] = await self.genre_repo.list(filters=filters)
        if genres:
            return genres
        raise GenresNotFoundError
