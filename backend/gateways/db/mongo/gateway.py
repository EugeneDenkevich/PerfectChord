from uuid import UUID

from backend.domain.models import Song
from backend.gateways.db.nosql_gateway import NoSQLGateway


class MongoGateway(NoSQLGateway):
    """Реализвация интерфейса гейтвея для работы с MongoDB"""

    async def save_song(  # type: ignore[empty-body]
        self,
        title: str,
        author: str | UUID,
        body: dict[int, str],
    ) -> Song:
        ...


    async def get_song_by_id(self, song_id: UUID) -> Song:  # type: ignore[empty-body]
        ...


    async def get_songs(  # type: ignore[empty-body]
        self,
        limit: int,
        offset: int,
    ) -> Song:
        ...


    async def update(  # type: ignore[empty-body]
        self,
        song_id: UUID,
        title: str,
        author: str | UUID,
        body: dict[int, str],
    ) -> Song:
        ...


    async def delete_song_by_id(self, song_id: UUID) -> Song:  # type: ignore[empty-body]
        ...
