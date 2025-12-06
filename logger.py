# logger.py
"""
Very simple logging helpers for the project.
"""

from utils import current_timestamp


def _log(level: str, message: str) -> None:
    ts = current_timestamp()
    print(f"[{ts}] [{level}] {message}")


def log_info(message: str) -> None:
    _log("INFO", message)


def log_warning(message: str) -> None:
    _log("WARNING", message)


def log_error(message: str) -> None:
    _log("ERROR", message)
