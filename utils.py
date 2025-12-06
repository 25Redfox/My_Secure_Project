# utils.py
"""
Project utilities: timestamp + masking.
"""

import datetime


def current_timestamp() -> str:
    return datetime.datetime.utcnow().isoformat() + "Z"


def mask_key(key: str) -> str:
    if not key or len(key) < 6:
        return "***"
    return key[:3] + "***" + key[-4:]
