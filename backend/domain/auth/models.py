from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from backend.domain.auth.constants import REFRESH_EXPIRATION
from backend.domain.base import Base, datetime_now


def datetime_refresh_expired() -> datetime:
    return datetime_now() + REFRESH_EXPIRATION


class Tokens(BaseModel):
    """Токены пользователя"""

    access_token: str
    refresh_token: str
    refresh_token_expiration_time: int


class RefreshToken(Base):
    """Refresh токен пользователя"""

    expired_at: Optional[datetime] = Field(default_factory=datetime_refresh_expired)
    user_id: Optional[UUID] = None
