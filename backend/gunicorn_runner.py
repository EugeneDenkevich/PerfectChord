from typing import Any

from gunicorn.app.base import BaseApplication
from gunicorn.util import import_app
from uvicorn.workers import UvicornWorker as BaseUvicornWorker

try:
    import uvloop  # noqa: WPS433
except ImportError:
    uvloop = None  # type: ignore  # noqa: WPS440


class UvicornWorker(BaseUvicornWorker):
    """
    Конфигурация воркеров uvicorn.

    Наследуемся от UvicornWorker (BaseUvicornWorker - это алиас! см. импорты)
    и определяем доп. параметры класса. По другому эти параметры в gunicorn не
    прокинуть.
    """

    CONFIG_KWARGS = {  # noqa: WPS115
        "loop": "uvloop" if uvloop is not None else "asyncio",
        "http": "httptools",
        "lifespan": "on",
        "factory": True,
        "proxy_headers": False,
    }


class GunicornApplication(BaseApplication):  # type: ignore[misc]
    """
    Кастомное приложение gunicorn.

    Приложение для старта gunicorn сервера
    с кастомными воркерами uvicorn-а.
    """

    def __init__(  # noqa: WPS211
        self,
        app: str,
        host: str,
        port: int,
        workers: int,
        **kwargs: Any,
    ):
        self.options = {
            "bind": f"{host}:{port}",
            "workers": workers,
            "worker_class": "backend.gunicorn_runner.UvicornWorker",
            **kwargs,
        }
        self.app = app
        super().__init__()

    def load_config(self) -> None:
        """
        Загрузка конфига веб-сервера.

        Установка параметров для главного процесса gunicorn.
        Только тех, которые сможет обрабатывать gunicorn.
        Если будут добавлены параметры, которые gunicorn не распознает -
        gunicorn упадёт с ошибкой.
        """
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self) -> Any:
        """
        Загрузить текущее приложение.

        Gunicorn загружает приложение, основываясь на том
        что возвращает этот метод. А возвращает он python путь к
        фабрике приложений.

        :returns: Python путь к фабрике приложений.
        """
        return import_app(self.app)
