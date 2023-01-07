from tortoise import fields, models

from common.orm import QBuilder, AnnotationBuilder
from common.orm.mixins import GenericMixin
from ..entities import BaseGenreRepo


class Genre(models.Model):
    """
    Модель жанра книги
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200, unique=True)

    books: fields.ManyToManyRelation["Book"]

    def __str__(self):
        return self.name

    class Meta:
        table = 'genres'


class GenreRepo(BaseGenreRepo, GenericMixin):
    """
    Репозиторий жанров
    """
    model = Genre
    q_builder: QBuilder = QBuilder(Genre)
    a_builder: AnnotationBuilder = AnnotationBuilder(Genre)
