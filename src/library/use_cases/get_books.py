from ..repos import BookRepo, Book
from ..exceptions import BookNotFoundError


class GetBooksCase:
    """
    Кейс получения книг(и)
    """

    def __init__(self) -> None:
        self.book_repo: BookRepo = BookRepo()

    async def __call__(self, book_id: int = None):
        filters: dict = dict()

        if book_id:
            filters = dict(id=book_id)

        books: list[Book] = await self.book_repo.list(filters=filters)
        if books:
            return books
        raise BookNotFoundError
