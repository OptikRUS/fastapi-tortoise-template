from enum import Enum
from pydantic import BaseModel, UUID4


class Token(BaseModel):
    access_token: str


class UserType(str, Enum):
    ANY = "any_user"
    ADMIN = "admin"
