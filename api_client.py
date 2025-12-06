# api_client.py
"""
Fake API client used for the CTF scenario.

This does not perform real HTTP calls. It just simulates
what a client would do with an API key.
"""

from security import describe_key


class APIClient:
    def __init__(self, api_key: str, endpoint: str) -> None:
        self.api_key = api_key
        self.endpoint = endpoint

    def health_check(self) -> str:
        """
        Fake health check. In a real case, this would:
        - Send an HTTP request to self.endpoint + "/health"
        - Include self.api_key in an Authorization header
        """
        key_desc = describe_key(self.api_key)
        return f"Connected to {self.endpoint} with {key_desc}"
