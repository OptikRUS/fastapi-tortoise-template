from ..repos import AuthorRepo, Author
from ..exceptions import AuthorsNotFoundError


class GetAuthorCase:
    """
    Кейс получения автора(ов)
    """

    def __init__(self) -> None:
        self.author_repo: AuthorRepo = AuthorRepo()

    async def __call__(self, author_id: int = None) -> list[Author]:
        filters: dict = dict()

        if author_id:
            filters = dict(id=author_id)

        authors: list[Author] = await self.author_repo.list(filters=filters)
        if authors:
            return authors
        raise AuthorsNotFoundError
