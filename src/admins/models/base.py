from datetime import datetime

from pydantic import BaseModel, Field


class UserUpdateResponse(BaseModel):
    id: int
    username: str = Field("username")
    updated_at: datetime
    created_at: datetime
