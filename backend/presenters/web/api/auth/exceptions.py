from pydantic.dataclasses import dataclass

from backend.presenters.web.exceptions import (
    DetailedHTTPException,
    Forbidden,
    NotFound,
    Unauthorized,
)


@dataclass
class LoginError(DetailedHTTPException):
    detail: str = "Ошибка при попытке авторизации"


@dataclass
class RefreshTokenError(DetailedHTTPException):
    detail: str = "Ошибка при обновлении токенов"


@dataclass
class InvalidCredentialsHTTPError(Unauthorized):
    detail: str = "Неправильные логин или пароль"


@dataclass
class InvalidRefreshTokenHTTPError(Unauthorized):
    detail: str = "Неправильный refresh токен"


@dataclass
class RefreshTokenExpiredHTTPError(Unauthorized):
    detail: str = "Срок действия refresh токена истёк"


@dataclass
class UserNotActiveHTTPError(Forbidden):
    detail: str = "Пользователь не активен"


@dataclass
class UserNotFoundHTTPError(NotFound):
    detail: str = "Пользователь не найден"


@dataclass
class RefreshTokenNotFoundHTTPError(NotFound):
    detail: str = "Refresh токен не найден"
