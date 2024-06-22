from pydantic import EmailStr, Field

from backend.domain.base import Base


class User(Base):
    """Пользователь"""

    username: str = Field(max_length=100)
    email: EmailStr
    password_hashed: str = Field(max_length=100)
