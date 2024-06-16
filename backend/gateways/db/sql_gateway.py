from abc import ABC, abstractmethod
from uuid import UUID

from backend.domain.models import Song


class SQLGateway(ABC):
    """Гейтвей для работы с SQL базами данных"""

    @abstractmethod
    async def get_user_by_id(self, user_id: UUID) -> Song:
        ...
