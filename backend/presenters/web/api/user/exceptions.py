from pydantic.dataclasses import dataclass

from backend.presenters.web.exceptions import BadRequest, DetailedHTTPException


@dataclass
class CreateUserHTTPError(DetailedHTTPException):
    detail: str = "Ошибка при создании пользователя"


@dataclass
class EmailExistsHTTPError(BadRequest):
    detail: str = "Пользователь с таким email уже существует"


@dataclass
class UsernameExistsHTTPError(BadRequest):
    detail: str = "Пользователь с таким username уже существует"


@dataclass
class GetUsersHTTPError(BadRequest):
    detail: str = "Ошибка при получении списка пользователей"
