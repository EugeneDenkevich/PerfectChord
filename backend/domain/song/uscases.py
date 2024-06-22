from uuid import UUID

from backend.domain.song.models import Song
from backend.gateways.db.builders import NoSQLGateway


class AddSongUseCase:
    """Добавление новой песни"""

    def __init__(
        self,
        nosql_gateway: NoSQLGateway,
    ) -> None:
        self.nosql_gateway = nosql_gateway

    async def __call__(
        self,
        title: str,
        author: str | UUID,
        body: dict[int, str],
    ) -> Song:
        return await self.nosql_gateway.save_song(
            title=title,
            author=author,
            body=body,
        )


class GetSongByIdUseCase:
    """Получение песни по её id"""

    def __init__(
        self,
        nosql_gateway: NoSQLGateway,
    ) -> None:
        self.nosql_gateway = nosql_gateway

    async def __call__(
        self,
        song_id: UUID,
    ) -> Song:
        return await self.nosql_gateway.get_song_by_id(song_id=song_id)


class GetSongsUseCase:
    """Получение списка песен"""

    def __init__(
        self,
        nosql_gateway: NoSQLGateway,
    ) -> None:
        self.nosql_gateway = nosql_gateway

    async def __call__(
        self,
        limit: int,
        offset: int,
    ) -> Song:
        return await self.nosql_gateway.get_songs(limit=limit, offset=offset)


class UpdateSongUseCase:
    """Обновление песни"""

    def __init__(
        self,
        nosql_gateway: NoSQLGateway,
    ) -> None:
        self.nosql_gateway = nosql_gateway

    async def __call__(
        self,
        song_id: UUID,
        title: str,
        author: str | UUID,
        body: dict[int, str],
    ) -> Song:
        return await self.nosql_gateway.update(
            song_id=song_id,
            title=title,
            author=author,
            body=body,
        )


class DeleteSongUseCase:
    """Удаление песни по id"""

    def __init__(
        self,
        nosql_gateway: NoSQLGateway,
    ) -> None:
        self.nosql_gateway = nosql_gateway

    async def __call__(
        self,
        song_id: UUID,
    ) -> Song:
        return await self.nosql_gateway.delete_song_by_id(song_id=song_id)
