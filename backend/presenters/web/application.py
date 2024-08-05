from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from backend.logging import configure_logging
from backend.presenters.web.api.router import api_router
from backend.presenters.web.lifetime import (
    register_shutdown_event,
    register_startup_event,
)
from backend.settings import settings


def get_app() -> FastAPI:
    """
    Создаёт FastAPI приложение.
    Главный конструктор FastAPI приложения.

    :return: FastAPI приложение.
    """
    configure_logging()
    app = FastAPI(
        title="Perfect Chord API",
        version="0.1.0",
        docs_url="/api/docs" if settings.enable_doc else None,
        redoc_url="/api/redoc" if settings.enable_doc else None,
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Добавление событий запуска и остановки приложения.
    register_startup_event(app)
    register_shutdown_event(app)

    # Главный API роутер.
    app.include_router(router=api_router, prefix="/api")

    return app
