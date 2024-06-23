from typing import List
from uuid import UUID

from backend.domain.song.models import Song
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
        limit: int | None,
        offset: int | None,
    ) -> List[Song]:
        ...


    async def update(  # type: ignore[empty-body]
        self,
        song_id: UUID,
        title: str | None,
        author: str | UUID | None,
        body: dict[int, str] | None,
    ) -> Song:
        ...


    async def delete_song_by_id(self, song_id: UUID) -> None:  # type: ignore[empty-body]
        ...
