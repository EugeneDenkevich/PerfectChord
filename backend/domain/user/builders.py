from typing import Annotated

from fastapi import Depends

from backend.domain.user.services import UserServiceD
from backend.domain.user.uscases import (
    CreateUserUseCase,
    GetUsersUseCase,
)
from backend.gateways.db.builders import SQLGatewayD


def build_create_user_usecase(
    sql_gateway: SQLGatewayD,
    user_service: UserServiceD,
) -> CreateUserUseCase:
    return CreateUserUseCase(sql_gateway=sql_gateway, user_service=user_service)


CreateUserUseCaseD = Annotated[CreateUserUseCase, Depends(build_create_user_usecase)]


def build_get_users_usecase(
    sql_gateway: SQLGatewayD,
) -> GetUsersUseCase:
    return GetUsersUseCase(sql_gateway=sql_gateway)


GetUsersUseCaseD = Annotated[GetUsersUseCase, Depends(build_get_users_usecase)]
