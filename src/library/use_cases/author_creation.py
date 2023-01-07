from ..models import CreateAuthorRequest
from ..repos import AuthorRepo, Author
from ..exceptions import AuthorAlreadyExistError


class AuthorCreationCase:
    """
    Кейс создания автора
    """

    def __init__(self) -> None:
        self.author_repo: AuthorRepo = AuthorRepo()

    async def __call__(self, author: CreateAuthorRequest) -> Author:
        filters: dict = dict(
            first_name__iexact=author.first_name,
            last_name__iexact=author.last_name,
            patronymic_name__iexact=author.patronymic_name,
        )

        author_exist: bool = await self.author_repo.exists(filters=filters)
        if author_exist:
            raise AuthorAlreadyExistError
        new_author: Author = await self.author_repo.create(author.dict())
        return new_author
