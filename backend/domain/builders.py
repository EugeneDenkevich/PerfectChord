from typing import Annotated

from fastapi import Depends

from backend.domain.uscases import AddSongUseCase
from backend.gateways.db.builders import NoSQLGatewayD, SQLGatewayD


def build_add_song_usecase(
    sql_gateway: SQLGatewayD,
    nosql_gateway: NoSQLGatewayD,
) -> AddSongUseCase:
    return AddSongUseCase(sql_gateway=sql_gateway, nosql_gateway=nosql_gateway)


AddSongUseCaseD = Annotated[AddSongUseCase, Depends(build_add_song_usecase)]
