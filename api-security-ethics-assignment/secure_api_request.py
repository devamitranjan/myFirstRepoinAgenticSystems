import os
import sys
from pathlib import Path
from typing import Optional

import requests
from dotenv import load_dotenv

# Repo root and assignment dir (script may be run from either cwd)
_ROOT = Path(__file__).resolve().parent.parent
_ASSIGNMENT_DIR = Path(__file__).resolve().parent
load_dotenv(_ROOT / ".env")
load_dotenv(_ASSIGNMENT_DIR / ".env")

API_URL = "https://api.example.com/data"



def get_api_key() -> Optional[str]:
    return os.getenv("API_KEY_ENV_VAR")


def secure_api_request() -> None:
    api_key = get_api_key()
    if not api_key:
        print(f"Missing API key. Please set the API_KEY_ENV_VAR environment variable.")
        sys.exit(1)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
    }

    try:
        response = requests.get(API_URL, headers=headers, timeout=10)
    except requests.RequestException as exc:
        print(f"Request failed due to a network or configuration error: {exc}")
        sys.exit(1)

    if response.status_code == 200:
        try:
            data = response.json()
        except ValueError:
            print("Response was 200 but did not contain valid JSON.")
            sys.exit(1)
        print(data)
    elif response.status_code == 429:
        print("Rate limit reached. Try again later.")
    else:
        print("Request failed", response.status_code)


if __name__ == "__main__":
    secure_api_request()

