from typing import Awaitable, Callable

from fastapi import FastAPI


def register_startup_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:
    """
    Запускает действия при старте приложения.

    :param app: Экземпляр приложения.
    :return: Функция для запуска действий при старте приложения.
    """

    @app.on_event("startup")
    async def _startup() -> None:  # noqa: WPS430
        app.middleware_stack = None
        app.middleware_stack = app.build_middleware_stack()

    return _startup


def register_shutdown_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:
    """
    Запускает действия при остановке приложения.

    :param app: Экземпляр приложения.
    :return: Функция для запуска действий при остановке приложения.
    """

    @app.on_event("shutdown")
    async def _shutdown() -> None:  # noqa: WPS430
        ...

    return _shutdown
