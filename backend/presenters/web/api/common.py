import logging
from traceback import format_exc

from backend.settings import settings


def log_error() -> None:
    logging.error(
        f"Error while user logging:\nNooo...{try_get_vader()}{format_exc()}",
    )


def try_get_vader() -> str:
    try:
        with open(settings.vader_path, "r") as f:
            return "\n" + f.read() + "\n"
    except Exception:
        return ""
