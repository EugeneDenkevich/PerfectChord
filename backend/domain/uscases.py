from typing import Annotated
from uuid import UUID

from fastapi import Depends

from backend.domain.models import Song
from backend.gateways.db import NoSQLGateway, NoSQLGatewayD, SQLGateway, SQLGatewayD


class AddSongUseCase:
    """Добавление новой песни"""

    def __init__(
        self,
        sql_gateway: SQLGateway,
        nosql_gateway: NoSQLGateway,
    ) -> None:
        self.sql_gateway = sql_gateway
        self.nosql_gateway = nosql_gateway

    async def __call__(
        self,
        title: str,
        author: str | UUID,
        body: dict[int, str],
    ) -> Song:
        return await self.nosql_gateway.save_song(
            title=title,
            author=(
                await self.sql_gateway.get_user_by_id(user_id=author)
                if isinstance(author, UUID) else author
            ),
            body=body,
        )


def build_add_song_usecase(
    sql_gateway: SQLGatewayD,
    nosql_gateway: NoSQLGatewayD,
) -> AddSongUseCase:
    return AddSongUseCase(sql_gateway=sql_gateway, nosql_gateway=nosql_gateway)


AddSongUseCaseD = Annotated[AddSongUseCase, Depends(build_add_song_usecase)]
