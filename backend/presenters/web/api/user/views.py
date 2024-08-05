import logging
from typing import Annotated, List, Union

from fastapi import APIRouter, Depends, status

from backend.domain.user.builders import CreateUserUseCaseD, GetUsersUseCaseD
from backend.domain.user.exceptions import EmailExistsError, UsernameExistsError
from backend.domain.user.models import User
from backend.presenters.web.api.dependencies import CurrentUserD
from backend.presenters.web.api.exceptions import (
    AccessTokenExpiredError,
    InvalidAccessTokenError,
)
from backend.presenters.web.api.user.exceptions import (
    CreateUserHTTPError,
    EmailExistsHTTPError,
    GetUsersHTTPError,
    UsernameExistsHTTPError,
)
from backend.presenters.web.api.user.schema import CreateUserInput, GetUsersInput

router = APIRouter()


@router.post(
    path="",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {"model": User},
        status.HTTP_400_BAD_REQUEST: {
            "model": Union[EmailExistsHTTPError, UsernameExistsHTTPError],
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": CreateUserHTTPError,
        },
    },
    response_model=User,
)
async def create_user(
    user_input: CreateUserInput,
    create_user_uc: CreateUserUseCaseD,
) -> User:
    """
    Создание пользователя.

    :param user_input: Данные для создания пользователя.
    :param add_user: Юзкейс для создания пользователя.
    """
    try:
        return await create_user_uc(
            username=user_input.username,
            email=user_input.email,
            password=user_input.password,
        )
    except EmailExistsError:
        raise EmailExistsHTTPError()
    except UsernameExistsError:
        raise UsernameExistsHTTPError()
    except Exception as err:
        logging.error(f"Error while creating user: {err}")
        raise CreateUserHTTPError()


@router.get(
    path="",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": List[User]},
        status.HTTP_401_UNAUTHORIZED: {
            "model": Union[AccessTokenExpiredError, InvalidAccessTokenError],
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": GetUsersHTTPError,
        },
    },
    response_model=List[User],
)
async def get_users(
    get_users_input: Annotated[GetUsersInput, Depends()],
    get_users_uc: GetUsersUseCaseD,
    _: CurrentUserD,
) -> List[User]:
    """
    Получение списка пользователей.

    :param add_user: Юзкейс для получения списка пользователей.
    :param _: Текущий пользователь.
    """
    try:
        return await get_users_uc(
            limit=get_users_input.limit,
            offset=get_users_input.offset,
        )
    except Exception as err:
        logging.error(f"Error while getting user: {err}")
        raise GetUsersHTTPError()
