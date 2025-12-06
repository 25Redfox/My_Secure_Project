# main.py
"""
Main entry for My_Secure_Project.
"""

from config import API_KEY, API_ENDPOINT
from api_client import APIClient
from logger import log_info, log_error


def main():
    log_info("Launching client…")

    if not API_KEY:
        log_error("No API key found. Exiting.")
        return

    client = APIClient(api_key=API_KEY, endpoint=API_ENDPOINT)

    try:
        status = client.health_check()
        log_info(status)
    except Exception as e:
        log_error(f"Health check failed → {e}")


if __name__ == "__main__":
    main()
