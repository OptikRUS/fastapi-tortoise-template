from .schemas import CreateGenre, GenreResponse, CreateAuthor, AuthorResponse, CreateBook, BookResponse
from .models import Genre, Author, Book
from .exceptions import (
    GenreAlreadyExistError, GenresNotFoundError, AuthorAlreadyExistError, AuthorsNotFoundError,
    BookAlreadyExistError, BooksNotFoundError
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

        genres = await Genre.filter(id__in=book.genres_id)
        if not genres:
            raise GenresNotFoundError

        authors = await Author.filter(id__in=book.authors_id)
        if not authors:
            raise AuthorsNotFoundError

        book_exist = await Book.exists(title__iexact=book.title)
        if book_exist:
            raise BookAlreadyExistError

        new_book = await Book.create(**book.dict())
        await new_book.authors.add(*authors)
        await new_book.genres.add(*genres)
        await new_book.save()

        created_book = await Book.get(id=new_book.id).prefetch_related('authors', 'genres')

        return BookResponse.from_orm(created_book)


class GetBooksCase:
    """
    Кейс получения всех книг
    """

    async def __call__(self):

        all_books = await Book.all().prefetch_related('authors', 'genres')
        if all_books:
            return all_books

        raise BooksNotFoundError
