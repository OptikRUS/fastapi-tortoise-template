from tortoise import fields, models

from .exceptions import AuthorFullNameError


class Authors(models.Model):
    """
    Модель автора
    """
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    patronymic_name = fields.CharField(max_length=50)
    date_of_birth = fields.DateField(null=True)
    date_of_death = fields.DateField(null=True)

    @property
    def full_name(self) -> str:
        """
        ФИО автора
        """
        if self.first_name and self.last_name and self.patronymic_name:
            return f"{self.last_name} {self.first_name} {self.patronymic_name}"

    def __str__(self):
        if self.full_name:
            return self.full_name
        raise AuthorFullNameError

    class PydanticMeta:
        computed = ["full_name"]


class Genres(models.Model):
    """
    Модель жанра книги
    """
    name = fields.CharField(max_length=200)

    def __str__(self):
        return self.name


class Books(models.Model):
    """
    Модель книги
    """
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200)
    author: fields.ManyToManyRelation[Authors] = fields.ManyToManyField(
        'models.Authors', related_name='books', on_delete=fields.SET_NULL, through='books_authors'
    )
    summary = fields.TextField()
    genre: fields.ManyToManyRelation[Genres] = fields.ManyToManyField(
        'models.Genres', related_name='books', on_delete=fields.SET_NULL, through='books_genres'
    )
    user = fields.ForeignKeyField('models.Users', related_name='books')
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.title
