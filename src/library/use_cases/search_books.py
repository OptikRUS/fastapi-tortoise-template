from ..repos import BookRepo, Book
from ..exceptions import BooksNotFoundError


class SearchBookCase:
    """
    Кейс поиска книг по названию или описанию
    """

    def __init__(self) -> None:
        self.book_repo: BookRepo = BookRepo()

    async def __call__(self, search_book: str):
        or_filters: list = [
            dict(title__icontains=search_book),
            dict(summary__icontains=search_book)
        ]
        q_filters: list = [
            self.book_repo.q_builder(or_filters=or_filters)
        ]

        found_books: list[Book] = await self.book_repo.list(q_filters=q_filters)

        if not found_books:
            raise BooksNotFoundError

        books_response = dict(
            count=len(found_books),
            found_books=found_books
        )
        return books_response
