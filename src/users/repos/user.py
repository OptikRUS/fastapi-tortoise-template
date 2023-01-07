from tortoise import fields
from tortoise.models import Model

from common.orm import QBuilder, AnnotationBuilder
from common.orm.mixins import GenericMixin
from common.models import TimeBasedMixin
from ..entities import BaseUserRepo


class User(Model, TimeBasedMixin):
    """
    Модель пользователя
    """

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    patronymic_name = fields.CharField(max_length=50, null=True)
    email = fields.CharField(null=False, max_length=255, unique=True)
    phone = fields.CharField(null=True, max_length=15, unique=True)
    password = fields.CharField(max_length=128, null=True)
    is_active = fields.BooleanField(default=True)
    is_approved = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)

    @property
    def full_name_or_username(self) -> str:
        """
        Полное имя (ФИО)
        """
        if self.first_name and self.last_name and self.patronymic_name:
            return f"{self.last_name} {self.first_name} {self.patronymic_name}"
        return self.username

    def __str__(self):
        return self.username

    class PydanticMeta:
        computed = ["full_name_or_username"]
        exclude = ["password"]

    class Meta:
        table = "users"


class UserRepo(BaseUserRepo, GenericMixin):
    """
    Репозиторий пользователя
    """
    model = User
    q_builder: QBuilder = QBuilder(User)
    a_builder: AnnotationBuilder = AnnotationBuilder(User)
