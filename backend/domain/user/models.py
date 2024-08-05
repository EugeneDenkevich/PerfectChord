from typing import Optional

from pydantic import EmailStr, Field

from backend.domain.base import Base


class User(Base):
    """Пользователь"""

    username: str = Field(max_length=36)
    email: EmailStr
    password_hashed: str = Field(min_length=8, max_length=256)
    is_active: Optional[bool] = Field(default=False)
