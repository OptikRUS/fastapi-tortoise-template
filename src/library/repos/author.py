from tortoise import fields, models

from common.orm import QBuilder, AnnotationBuilder
from common.orm.mixins import GenericMixin
from ..entities import BaseAuthorRepo
from ..exceptions import AuthorFullNameError


class Author(models.Model):
    """
    Модель автора
    """
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    patronymic_name = fields.CharField(max_length=50, null=True)
    date_of_birth = fields.DateField(null=True)
    date_of_death = fields.DateField(null=True)

    books: fields.ForeignKeyRelation["Book"]

    @property
    def full_name(self) -> str:
        """
        ФИО автора
        """
        if self.first_name and self.last_name and self.patronymic_name:
            return f"{self.last_name} {self.first_name} {self.patronymic_name}"
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        if self.full_name:
            return self.full_name
        raise AuthorFullNameError

    class PydanticMeta:
        computed = ["full_name"]
        # Если мы должны исключить необработанные поля (те, которые имеют суффиксы _id) отношений
        exclude_raw_fields: bool = True

    class Meta:
        table = 'authors'
        unique_together = ('first_name', 'last_name')


class AuthorRepo(BaseAuthorRepo, GenericMixin):
    """
    Репозиторий авторов
    """
    model = Author
    q_builder: QBuilder = QBuilder(Author)
    a_builder: AnnotationBuilder = AnnotationBuilder(Author)
