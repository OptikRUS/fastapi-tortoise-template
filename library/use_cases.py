from .schemas import CreateGenre, GenreResponse, CreateAuthor, AuthorResponse, CreateBook, BookResponse
from .models import Genre, Author, Book
from .exceptions import (
    GenreAlreadyExistError, GenresNotFoundError, AuthorAlreadyExistError, AuthorsNotFoundError, GenreNotFoundError,
    AuthorNotFoundError, BookAlreadyExistError
)


class GenreCreationCase:
    """
    Кейс создания жанра
    """

    async def __call__(self, genre: CreateGenre) -> GenreResponse:
        genre_exist = await Genre.exists(name__iexact=genre.name)

        if genre_exist:
            raise GenreAlreadyExistError
        new_genre = await Genre.create(**genre.dict())
        return GenreResponse.from_orm(new_genre)


class GetGenresCase:
    """
    Кейс получения всех жанров
    """

    async def __call__(self):
        all_genres = await Genre.all()
        if all_genres:
            return all_genres
        raise GenresNotFoundError


class AuthorCreationCase:
    """
    Кейс создания автора
    """

    async def __call__(self, author: CreateAuthor) -> AuthorResponse:
        author_exist = await Author.exists(
            first_name__iexact=author.first_name,
            last_name__iexact=author.last_name,
            patronymic_name__iexact=author.patronymic_name,
        )

        if author_exist:
            raise AuthorAlreadyExistError
        new_author = await Author.create(**author.dict())
        return AuthorResponse.from_orm(new_author)


class GetAuthorsCase:
    """
    Кейс получения всех авторов
    """

    async def __call__(self):
        all_authors = await Author.all()
        if all_authors:
            return all_authors
        raise AuthorsNotFoundError


class BookCreationCase:
    """
    Кейс создания книги
    """

    async def __call__(self, book: CreateBook) -> BookResponse:
        genre = await Genre.get_or_none(id=book.genre_id)
        if not genre:
            raise GenreNotFoundError

        author = await Author.get_or_none(id=book.author_id)
        if not author:
            raise AuthorNotFoundError

        book_exist = await Book.exists(title__iexact=book.title)

        if book_exist:
            raise BookAlreadyExistError

        new_book = await Book.create(**book.dict())
        await new_book.author.add(author)
        await new_book.genre.add(genre)
        await new_book.save()

        created_book = await Book.get(id=new_book.id).select_related("author", "genre")

        return BookResponse.from_orm(created_book)
