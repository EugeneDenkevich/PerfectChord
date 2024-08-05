class UserNotFoundError(Exception):
    """Пользователь с таким email не найден"""


class UserNotActiveError(Exception):
    """Пользователь не активен"""


class InvalidCredentialsError(Exception):
    """Неверные почта или пароль"""


class RefreshTokenExpiredError(Exception):
    """Refresh токен просрочен"""


class InvalidRefreshTokenError(Exception):
    """Неверный refresh токен"""


class RefreshTokenNotFoundError(Exception):
    """Refresh токен не найден"""
