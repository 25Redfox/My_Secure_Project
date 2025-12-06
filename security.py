# security.py
"""
Security-related helpers.

In a real-world app, this is where you would handle input
validation, basic sanitization, and checks.
"""

from utils import mask_key


def is_api_key_suspicious(api_key: str) -> bool:
    """
    Dummy check: consider keys shorter than 10 chars as suspicious/bad.
    """
    return not api_key or len(api_key) < 10


def describe_key(api_key: str) -> str:
    """
    Return a human-readable description of the key without exposing it.
    """
    masked = mask_key(api_key)
    if is_api_key_suspicious(api_key):
        return f"API key looks weak or invalid: {masked}"
    return f"API key seems valid in format: {masked}"
