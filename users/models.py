from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Users(models.Model):
    """
    Модель пользователя
    """
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    patronymic_name = fields.CharField(max_length=50, null=True)
    email = fields.CharField(null=False, max_length=255)
    phone = fields.CharField(null=True, max_length=15)
    password = fields.CharField(max_length=128, null=True)
    is_active = fields.BooleanField(default=True)
    is_approved = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def full_name_or_username(self) -> str:
        """
        Полное имя (ФИО)
        """
        if self.first_name and self.last_name and self.patronymic_name:
            return f"{self.last_name} {self.first_name} {self.patronymic_name}"
        return self.username

    class PydanticMeta:
        computed = ["full_name_or_username"]
        exclude = ["password"]


# определение схем, но не такое гибкое
UserUpdate = pydantic_model_creator(
    Users, name="UserUpdate", exclude=("id", "is_active", "is_approved", "is_superuser"), exclude_readonly=True
)
UserResponse = pydantic_model_creator(Users, name="UserResponse", exclude_readonly=True)
UserForAdminResponse = pydantic_model_creator(Users, name="UsersForAdminResponse")
