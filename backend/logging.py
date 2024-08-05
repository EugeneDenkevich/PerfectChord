import logging
import sys
from typing import Union

from loguru import logger

from backend.settings import settings


class InterceptHandler(logging.Handler):
    """
    Дефолтный обработчик из примеров документации loguru.
    Этот обработчик перехватывает все логи и пропускает их через loguru.
    """

    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        """
        Отправка логов в loguru.

        :param record: Запись в лог.
        """
        try:
            level: Union[str, int] = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Поиск функции, создавшей логируемое сообщение.
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back  # type: ignore
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def configure_logging() -> None:  # pragma: no cover
    """Настройка логов."""
    intercept_handler = InterceptHandler()

    logging.basicConfig(handlers=[intercept_handler], level=logging.NOTSET)

    for logger_name in logging.root.manager.loggerDict:
        if logger_name.startswith("uvicorn."):
            logging.getLogger(logger_name).handlers = []

    # Замена дефолтного обработчика uvicorn-а
    logging.getLogger("uvicorn").handlers = [intercept_handler]
    logging.getLogger("uvicorn.access").handlers = [intercept_handler]

    # Установка вывода, уровня и формата логов.
    logger.remove()
    logger.add(
        sys.stdout,
        level=settings.log_level.value,
    )
