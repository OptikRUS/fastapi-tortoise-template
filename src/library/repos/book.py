from tortoise import fields, models
from tortoise.transactions import atomic

from common.orm import QBuilder, AnnotationBuilder
from common.orm.mixins import GenericMixin
from common.models import TimeBasedMixin
from ..entities import BaseBookRepo
from ..exceptions import BookCreationError


class Book(models.Model, TimeBasedMixin):
    """
    Модель книги
    """
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200, unique=True)
    author: fields.ForeignKeyRelation['Author'] = fields.ForeignKeyField(
        'models.Author', related_name='author', on_delete=fields.SET_NULL, null=True
    )
    summary = fields.TextField()
    genres: fields.ManyToManyRelation['Genre'] = fields.ManyToManyField(
        'models.Genre', related_name='genres', on_delete=fields.SET_NULL, through='books_genres'
    )

    def __str__(self):
        return self.title

    class Meta:
        table = 'books'


class BookRepo(BaseBookRepo, GenericMixin):
    """
    Репозиторий книг
    """
    model = Book
    q_builder: QBuilder = QBuilder(Book)
    a_builder: AnnotationBuilder = AnnotationBuilder(Book)

    @atomic()
    async def m2m_create(self, book_data: dict, genres: list["Genre"]) -> None:
        """
        Создание книги через М2М
        """
        if genres:
            try:
                created_book = await self.create(book_data)
                await created_book.genres.add(*genres)
                return created_book
            except Exception:
                raise BookCreationError
