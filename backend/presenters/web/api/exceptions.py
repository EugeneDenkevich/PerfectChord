from pydantic.dataclasses import dataclass

from backend.presenters.web.exceptions import Unauthorized


@dataclass
class AccessTokenExpiredError(Unauthorized):
    detail: str = "Сроке действия access токена истёк"


@dataclass
class InvalidAccessTokenError(Unauthorized):
    detail: str = "Неправильный access токен"
