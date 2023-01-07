from ..repos import BookRepo, Book, GenreRepo
from ..exceptions import BookNotFoundError


class GetBookDetailCase:
    """
    Кейс получения детальной информации книги
    """

    def __init__(self) -> None:
        self.book_repo: BookRepo = BookRepo()
        self.genre_repo: GenreRepo = GenreRepo()

    async def __call__(self, book_id: int):
        filters: dict = dict(id=book_id)
        book: Book = await self.book_repo.retrieve(filters=filters)
        if book:
            book_response = dict(
                book,
                author=await book.author,
                genres=await book.genres
            )
            return book_response
        raise BookNotFoundError
