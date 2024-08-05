import uvicorn

from backend.gunicorn_runner import GunicornApplication
from backend.settings import settings


def main() -> None:
    """Точка входа в приложение."""
    if settings.reload:
        uvicorn.run(
            "backend.presenters.web.application:get_app",
            workers=settings.workers_count,
            host=settings.host,
            port=settings.port,
            reload=settings.reload,
            log_level=settings.log_level.value.lower(),
            factory=True,
        )
    else:
        # Используем gunicorn в случае, если
        # выключена опция reload, т. к. у воркеров
        # Uvicorn эта опция не работает.
        GunicornApplication(
            "backend.presenters.web.application:get_app",
            host=settings.host,
            port=settings.port,
            workers=settings.workers_count,
            factory=True,
            accesslog="-",
            loglevel=settings.log_level.value.lower(),
            access_log_format='%r "-" %s "-" %Tf',  # noqa: WPS323
        ).run()


if __name__ == "__main__":
    main()
