from datetime import datetime

from pydantic import BaseModel, Field


class UserApprovedResponse(BaseModel):
    id: int
    username: str = Field("username")
    is_approved: bool
    updated_at: datetime
    created_at: datetime
