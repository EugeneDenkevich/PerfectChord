from pydantic import Field

from backend.domain.base import Base


class User(Base):
    """Пользователь"""

    username: str = Field(max_length=100)
    email: str = Field(max_length=100)
    password_hashed: str = Field(max_length=100)
    is_admin: bool = False


class Body(Base):
    """Тело песни"""

    text: str
    chords: dict[int, str]


class Song(Base):
    """Песня"""

    title: str = Field(max_length=100)
    author: str | User
    body: Body
