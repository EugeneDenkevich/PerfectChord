from datetime import datetime
from typing import Annotated
from uuid import UUID

import jwt
from fastapi import Security
from fastapi.security import APIKeyCookie, HTTPAuthorizationCredentials, HTTPBearer

from backend.domain.auth.credentials import PublicKeyD
from backend.domain.user.models import User
from backend.presenters.web.api.exceptions import (
    AccessTokenExpiredError,
    InvalidAccessTokenError,
)


def get_refresh_token_security() -> APIKeyCookie:
    return APIKeyCookie(name="refresh_token_cookie", auto_error=True)


def get_access_token_security() -> HTTPBearer:
    return HTTPBearer()


HTTPCredentialsD = Annotated[
    HTTPAuthorizationCredentials, Security(get_access_token_security()),
]


def build_current_user(
    credentials: HTTPCredentialsD,
    public_key: PublicKeyD,
) -> User:
    """
    Возвращает текущего пользователя

    :param credentials: Данные для авторизации.
    :returm: Текущий пользователь.
    """
    try:
        data = jwt.decode(
            jwt=credentials.credentials,
            key=public_key,
            algorithms=["RS256"],
        )
    except jwt.ExpiredSignatureError:
        raise AccessTokenExpiredError()
    except jwt.InvalidTokenError:
        raise InvalidAccessTokenError()
    if data.get("type") != "ACCESS_TOKEN":
        raise InvalidAccessTokenError()
    return User(
        id=UUID(data["sub"]),
        email=data["email"],
        created_at=datetime.fromisoformat(data["reg_date"]),
        updated_at=datetime.fromisoformat(data["upd_date"]),
        is_active=data["is_active"],
        username=data["username"],
        password_hashed="super_secret",
    )


CurrentUserD = Annotated[User, Security(build_current_user)]
