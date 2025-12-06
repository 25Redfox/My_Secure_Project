# utils.py
"""
Utility functions used across the project.
"""

import datetime


def current_timestamp() -> str:
    """Return current UTC time as ISO string."""
    return datetime.datetime.utcnow().isoformat() + "Z"


def mask_key(key: str) -> str:
    """
    Return a masked representation of a secret.
    Example:
        "abcdef123456" -> "abc***3456"
    """
    if not key or len(key) < 6:
        return "***"

    return key[:3] + "***" + key[-4:]
