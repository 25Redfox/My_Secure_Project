# logger.py
"""
Very simple logger for the project.
"""

from utils import current_timestamp


def _log(level: str, message: str) -> None:
    ts = current_timestamp()
    print(f"[{ts}] [{level}] {message}")


def log_info(msg: str) -> None:
    _log("INFO", msg)


def log_warning(msg: str) -> None:
    _log("WARNING", msg)


def log_error(msg: str) -> None:
    _log("ERROR", msg)
