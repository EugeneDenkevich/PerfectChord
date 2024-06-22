from typing import Annotated

from fastapi import Depends

from backend.domain.uscases import (
    AddSongUseCase,
    DeleteSongUseCase,
    GetSongByIdUseCase,
    GetSongsUseCase,
    UpdateSongUseCase,
)
from backend.gateways.db.builders import NoSQLGatewayD


def build_add_song_usecase(
    nosql_gateway: NoSQLGatewayD,
) -> AddSongUseCase:
    return AddSongUseCase(nosql_gateway=nosql_gateway)


AddSongUseCaseD = Annotated[AddSongUseCase, Depends(build_add_song_usecase)]


def build_get_song_by_id_usecase(
    nosql_gateway: NoSQLGatewayD,
) -> GetSongByIdUseCase:
    return GetSongByIdUseCase(nosql_gateway=nosql_gateway)


GetSongByIdUseCaseD = Annotated[
    GetSongByIdUseCase,
    Depends(build_get_song_by_id_usecase),
]


def build_get_songs_usecase(
    nosql_gateway: NoSQLGatewayD,
) -> GetSongsUseCase:
    return GetSongsUseCase(nosql_gateway=nosql_gateway)


GetSongsUseCaseD = Annotated[GetSongsUseCase, Depends(build_get_songs_usecase)]


def build_update_song_usecase(
    nosql_gateway: NoSQLGatewayD,
) -> UpdateSongUseCase:
    return UpdateSongUseCase(nosql_gateway=nosql_gateway)


UpdateSongUseCaseD = Annotated[UpdateSongUseCase, Depends(build_update_song_usecase)]


def build_delete_song_usecase(
    nosql_gateway: NoSQLGatewayD,
) -> DeleteSongUseCase:
    return DeleteSongUseCase(nosql_gateway=nosql_gateway)


DeleteSongUseCaseD = Annotated[DeleteSongUseCase, Depends(build_delete_song_usecase)]
