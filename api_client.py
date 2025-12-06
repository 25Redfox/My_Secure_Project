# api_client.py
"""
Fake API client used for the CTF scenario.

Simulates API communication safely.
"""

from security import describe_key


class APIClient:
    def __init__(self, api_key: str, endpoint: str) -> None:
        self.api_key = api_key
        self.endpoint = endpoint

    def health_check(self) -> str:
        """
        Fake health check that returns masked key information.
        """
        key_desc = describe_key(self.api_key)
        return f"Health OK → Endpoint: {self.endpoint} | Auth: {key_desc}"
