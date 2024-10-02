from annotated_types import MinLen, MaxLen
from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Annotated, Optional
from uuid import UUID

from enums import UserRoles


class User(BaseModel):
    id: UUID
    fullname: Optional[Annotated[str, MinLen(3), MaxLen(24)]] = None
    email: EmailStr
    password: str
    role: UserRoles = UserRoles.USER
    created_at: datetime
