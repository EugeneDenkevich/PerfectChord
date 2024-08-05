class EmailExistsError(Exception):
    """Пользователь с таким email уже существует"""


class UsernameExistsError(Exception):
    """Пользователь с таким username уже существует"""
