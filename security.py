# security.py
"""
Security-related helper functions.
"""

from utils import mask_key


def is_api_key_valid(api_key: str) -> bool:
    return bool(api_key) and len(api_key) >= 10


def describe_key(api_key: str) -> str:
    masked = mask_key(api_key)
    if is_api_key_valid(api_key):
        return f"Valid key ({masked})"
    return f"Weak or missing key ({masked})"
