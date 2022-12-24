from tortoise import fields, models

from .exceptions import AuthorFullNameError


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


class Book(models.Model):
    """
    Модель книги
    """
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200, unique=True)
    author: fields.ForeignKeyRelation[Author] = fields.ForeignKeyField(
        'models.Author', related_name='books', on_delete=fields.SET_NULL, null=True
    )
    summary = fields.TextField()
    genres: fields.ManyToManyRelation[Genre] = fields.ManyToManyField(
        'models.Genre', related_name='books', on_delete=fields.SET_NULL, through='books_genres'
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        table = 'books'
