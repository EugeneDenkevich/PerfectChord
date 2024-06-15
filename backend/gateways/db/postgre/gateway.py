from uuid import UUID

from backend.domain.models import Body, Song

from backend.gateways.db.gateway import DBGateway


class PostgresGateway(DBGateway):
    async def save_song(self, title: str, author: str | UUID, body: Body) -> Song:
        ...

    async def get_user_by_id(self, user_id: UUID) -> Song:
        ...
