from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from backend.domain.song.models import Song


class NoSQLGateway(ABC):
    """Гейтвей для работы с SQL базами данных"""

    @abstractmethod
    async def save_song(
        self,
        title: str,
        author: str | UUID,
        body: dict[int, str],
    ) -> Song:
        ...

    @abstractmethod
    async def get_song_by_id(self, song_id: UUID) -> Song:
        ...

    @abstractmethod
    async def get_songs(self, limit: int | None, offset: int | None) -> List[Song]:
        ...

    @abstractmethod
    async def update(
        self,
        song_id: UUID,
        title: str | None,
        author: str | UUID | None,
        body: dict[int, str] | None,
    ) -> Song:
        ...

    @abstractmethod
    async def delete_song_by_id(self, song_id: UUID) -> None:
        ...
