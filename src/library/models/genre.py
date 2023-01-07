from pydantic import Field

from ..entities import BaseGenreModel


class CreateGenre(BaseGenreModel):
    """
    Модель запроса создания жанра
    """

    name: str = Field("Жанр для книги", min_length=4, max_length=25)


class GenreResponse(CreateGenre):
    """
    Модель ответа для жанра
    """

    id: int

    class Config:
        orm_mode = True
