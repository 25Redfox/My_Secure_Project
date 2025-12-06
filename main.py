# main.py
"""
Entry point for My_Secure_Project.

This script simulates a simple client that uses
a secret API key from config.py to talk to an API endpoint.
"""

from config import API_KEY, API_ENDPOINT
from api_client import APIClient
from logger import log_info, log_error


def main():
    log_info("Starting My_Secure_Project client...")

    if not API_KEY:
        log_error("API key is missing! Exiting.")
        return

    client = APIClient(api_key=API_KEY, endpoint=API_ENDPOINT)

    try:
        status = client.health_check()
        log_info(f"API health check OK: {status}")
    except Exception as e:
        log_error(f"API health check failed: {e}")


if __name__ == "__main__":
    main()
