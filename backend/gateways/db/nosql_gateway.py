from abc import ABC, abstractmethod
from uuid import UUID

from backend.domain.models import Song


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
