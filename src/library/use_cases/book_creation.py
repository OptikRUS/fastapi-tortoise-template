from ..models import CreateBookRequest
from ..repos import BookRepo, GenreRepo, AuthorRepo
from ..exceptions import SomeGenreNotFoundError, BookAlreadyExistError, AuthorNotFoundError


class BookCreationCase:
    """
    Кейс создания книги
    """

    def __init__(self) -> None:
        self.book_repo: BookRepo = BookRepo()
        self.author_repo: AuthorRepo = AuthorRepo()
        self.genre_repo: GenreRepo = GenreRepo()

    async def __call__(self, book_data: CreateBookRequest):
        genres_filters: dict = dict(id__in=book_data.genres_id)
        found_genres = await self.genre_repo.list(filters=genres_filters)
        if not found_genres or len(found_genres) != len(book_data.genres_id):
            raise SomeGenreNotFoundError

        author_filters: dict = dict(id=book_data.author_id)
        author_exist: bool = await self.author_repo.exists(filters=author_filters)
        if not author_exist:
            raise AuthorNotFoundError

        book_filters: dict = dict(title__iexact=book_data.title)
        book_exist: bool = await self.book_repo.exists(filters=book_filters)
        if book_exist:
            raise BookAlreadyExistError

        new_book = await self.book_repo.m2m_create(book_data=book_data.dict(), genres=found_genres)
        book_filter: dict = dict(id=new_book.id)
        created_book = await self.book_repo.retrieve(filters=book_filter, related_fields=["author"])

        book_response: dict = dict(
            created_book,
            author=created_book.author,
            genres=await created_book.genres
        )
        return book_response
