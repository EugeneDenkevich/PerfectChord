from pydantic import Field

from backend.domain.base import Base
from backend.domain.user.models import User


class Song(Base):
    """Песня"""

    title: str = Field(max_length=100)
    author: str | User
    text: str
    chords: dict[int, str]
