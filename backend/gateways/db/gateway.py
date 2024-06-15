from abc import ABC, abstractmethod
from typing import Annotated
from uuid import UUID

from fastapi import Depends

from backend.domain.models import Body, Song
from backend.gateways.db.postgre.gateway import PostgresGateway


class DBGateway(ABC):
    """Гейтвей для работы с базами данных"""

    @abstractmethod
    async def save_song(self, title: str, author: str | UUID, body: Body) -> Song:
        ...
    
    @abstractmethod
    async def get_user_by_id(self, user_id: UUID) -> Song:
        ...


def build_db_gateway():
    return PostgresGateway()


DBGatewayD = Annotated[DBGateway, Depends(build_db_gateway)]
