from enum import Enum
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str


class UserType(str, Enum):
    ANY = "any"
    ADMIN = "admin"
