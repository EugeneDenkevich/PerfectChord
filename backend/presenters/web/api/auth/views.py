import logging
from typing import Union

from fastapi import APIRouter, Response, Security, status

from backend.domain.auth.builders import GetTokensUseCaseD, RefreshTokensUseCaseD
from backend.domain.auth.exceptions import (
    InvalidCredentialsError,
    InvalidRefreshTokenError,
    RefreshTokenExpiredError,
    RefreshTokenNotFoundError,
    UserNotActiveError,
    UserNotFoundError,
)
from backend.presenters.web.api.auth.exceptions import (
    InvalidCredentialsHTTPError,
    InvalidRefreshTokenHTTPError,
    LoginError,
    RefreshTokenError,
    RefreshTokenExpiredHTTPError,
    RefreshTokenNotFoundHTTPError,
    UserNotActiveHTTPError,
    UserNotFoundHTTPError,
)
from backend.presenters.web.api.auth.schemas import AccessToken, LoginInput
from backend.presenters.web.api.common import log_error
from backend.presenters.web.api.dependencies import get_refresh_token_security

router = APIRouter()


@router.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": AccessToken},
        status.HTTP_401_UNAUTHORIZED: {"model": InvalidCredentialsHTTPError},
        status.HTTP_403_FORBIDDEN: {"model": UserNotActiveHTTPError},
        status.HTTP_404_NOT_FOUND: {"model": UserNotFoundHTTPError},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": LoginError},
    },
)
async def login(
    response: Response,
    login_input: LoginInput,
    get_tokens_uc: GetTokensUseCaseD,
) -> AccessToken:
    """
    Вход в аккаунт.

    :param response: FastAPI ответ для установки куки.
    :param login_input: Данные для входа в аккаунт.
    :param get_tokens_uc: Юзкейс для получения токенов пользователя.
    :return: Токен доступа пользователя.
    """
    try:
        tokens = await get_tokens_uc(
            email=login_input.email,
            password=login_input.password,
        )
    except UserNotFoundError:
        raise UserNotFoundHTTPError()
    except UserNotActiveError:
        raise UserNotActiveHTTPError()
    except InvalidCredentialsError:
        raise InvalidCredentialsHTTPError()
    except Exception:
        log_error()
        raise LoginError()
    logging.info(f"User was logged: {login_input.email}")

    response.set_cookie(
        key="refresh_token_cookie",
        value=tokens.refresh_token,
        httponly=True,
        max_age=tokens.refresh_token_expiration_time,
        path="/api/auth/token/refresh",
    )

    return AccessToken(access_token=tokens.access_token)


@router.post(
    path="/token/refresh",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_200_OK: {"model": AccessToken},
        status.HTTP_401_UNAUTHORIZED: {
            "model": Union[InvalidRefreshTokenHTTPError, RefreshTokenExpiredHTTPError],
        },
        status.HTTP_404_NOT_FOUND: {
            "model": Union[UserNotFoundHTTPError, RefreshTokenNotFoundHTTPError],
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": RefreshTokenError},
    },
)
async def refresh_token(
    response: Response,
    refresh_tokens_uc: RefreshTokensUseCaseD,
    current_refresh_token: str = Security(get_refresh_token_security()),
) -> AccessToken:
    """
    Обновление токенов.

    :param response: FastAPI ответ для установки куки.
    :param refresh_token_uc: Юзкейс для обновления токенов.
    :param current_refresh_token: Текущий refresh токен.
    """
    try:
        tokens = await refresh_tokens_uc(refresh_t=current_refresh_token)
    except InvalidRefreshTokenError:
        raise InvalidRefreshTokenHTTPError()
    except RefreshTokenExpiredError:
        raise RefreshTokenExpiredHTTPError()
    except UserNotFoundError:
        raise UserNotFoundHTTPError()
    except RefreshTokenNotFoundError:
        raise RefreshTokenNotFoundHTTPError()
    except Exception:
        log_error()
        raise RefreshTokenError()
    logging.debug("Token refreshed")

    response.set_cookie(
        key="refresh_token_cookie",
        value=tokens.refresh_token,
        httponly=True,
        max_age=tokens.refresh_token_expiration_time,
        path="/api/auth/token/refresh",
    )

    return AccessToken(access_token=tokens.access_token)
