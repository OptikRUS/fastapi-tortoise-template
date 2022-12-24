from typing import Optional
from tortoise.expressions import Q

from .schemas import CreateGenre, GenreResponse, CreateAuthor, AuthorResponse, CreateBook, BookDetailResponse
from .models import Genre, Author, Book
from library import exceptions as exc


class GenreCreationCase:
    """
    Кейс создания жанра
    """

    async def __call__(self, genre: CreateGenre) -> GenreResponse:
        genre_exist = await Genre.exists(name__iexact=genre.name)

        if genre_exist:
            raise exc.GenreAlreadyExistError
        new_genre = await Genre.create(**genre.dict())
        return GenreResponse.from_orm(new_genre)


class GetGenresCase:
    """
    Кейс получения жанра(ов)
    """

    async def __call__(self, genre_id: Optional[int]):
        if not genre_id:
            return await Genre.all()

        genre = await Genre.filter(id=genre_id)
        if genre:
            return genre
        raise exc.GenreNotFoundError


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
            raise exc.AuthorAlreadyExistError
        new_author = await Author.create(**author.dict())
        return AuthorResponse.from_orm(new_author)


class GetAuthorCase:
    """
    Кейс получения автора(ов)
    """

    async def __call__(self, author_id: Optional[int]):
        if not author_id:
            return await Author.all()

        author = await Author.filter(id=author_id)
        if author:
            return author
        raise exc.AuthorNotFoundError


class BookCreationCase:
    """
    Кейс создания книги
    """

    async def __call__(self, book: CreateBook) -> BookDetailResponse:

        genres = await Genre.filter(id__in=book.genres_id)
        if not genres:
            raise exc.GenresNotFoundError

        author = await Author.filter(id=book.author_id)
        if not author:
            raise exc.AuthorNotFoundError

        book_exist = await Book.exists(title__iexact=book.title)
        if book_exist:
            raise exc.BookAlreadyExistError

        new_book = await Book.create(**book.dict())

        # добавление зависимости m2m
        await new_book.genres.add(*genres)
        await new_book.save()

        created_book = await Book.get(id=new_book.id).select_related('author')

        book_response = dict(
            created_book,
            author=created_book.author,  # авторы уже подтянуты через select_related
            genres=await created_book.genres  # отдельные запросы в бд для m2m
        )
        return BookDetailResponse(**book_response)


class GetBooksCase:
    """
    Кейс получения книг(и)
    """

    async def __call__(self, book_id: Optional[int]):

        if not book_id:
            all_books = await Book.all()
            if all_books:
                return all_books
            raise exc.BooksNotFoundError

        book = await Book.filter(id=book_id)
        if book:
            return book
        raise exc.BookNotFoundError


class GetBookDetailCase:

    async def __call__(self, book_id: int):

        book = await Book.get_or_none(id=book_id)
        if book:
            book_response = dict(
                book,
                author=await book.author,
                genres=await book.genres
            )
            return book_response
        raise exc.BookNotFoundError


class SearchBookCase:
    """
    Кейс поиска книг по названию или описанию
    """

    async def __call__(self, search_book: str):
        found_books = list()

        books_search = await Book.filter(
            Q(title__icontains=search_book) |
            Q(summary__icontains=search_book)
        )
        if books_search:
            for book in books_search:
                found_books.append(
                    dict(
                        book,
                        author=await book.author,  # подтягивание авторов без select_related
                        genres=await book.genres
                    )
                )
            books_response = dict(
                count=len(found_books),
                found_books=found_books
            )
            return books_response
        raise exc.BookNotFoundError
