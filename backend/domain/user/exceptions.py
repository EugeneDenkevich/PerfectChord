class NoPasswordOrLoginError(Exception):
    """Ошибка при отсутствии логина или пароля"""

    message = "Не предоставлен логин или пароль"
