"""CLI client used by the GitHub Action to communicate with the backend."""

import requests
import sys
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


BACKEND_URL = os.getenv("BACKEND_URL") or "http://localhost:8000/optimize-code"

class CLIClient:
    """Client responsible for communicating with the backend API."""

    def __init__(self, backend_url: str):
        """
        Args:
            backend_url (str): URL of the backend API.
        """
        self.backend_url = backend_url

    def send_code(self, filename: str, code: str) -> None:
        """Send a single file to the backend for optimization.

        Args:
            filename (str): Name of the file.
            code (str): Source code content.
        """
        try:
            payload = {
                "filename": filename,
                "code": code
            }

            response = requests.post(self.backend_url, json=payload)

            if response.status_code != 200:
                logger.error(f"{filename}: {response.status_code}")
                logger.error(response.text)
                return

            result = response.json()

            self._print_result(result)
        except requests.exceptions.ConnectionError:
            logger.error("Backend is not reachable.")
            sys.exit(1)

    def _print_result(self, result: dict) -> None:
        """Print the result in a readable format.

        Args:
            result (dict): Response from backend.
        """

        filename = result["filename"]
        optimized = result["optimized"]

        print(f"\n--- {filename} ---")

        if optimized:
            print("[INFO] Code was optimized")
            print("[LINT ERRORS]")
            for error in result["lint_errors"]:
                print(f"- {error}")
        else:
            print("[INFO] No issues found")

        # print("\n[CODE OUTPUT]")
        # print(result["code"])

        if optimized:
            self._save_optimized_code(filename, result["code"])

    def _save_optimized_code(self, filename: str, code: str) -> None:
        """Save optimized code to a new file.

        Args:
            filename (str): Original file name.
            code (str): Optimized Python code.
        """

        new_filename = filename.replace(".py", "_optimized.py")

        with open(new_filename, "w", encoding="utf-8") as file:
            file.write(code)

        print(f"[INFO] Optimized file saved as: {new_filename}")

def read_file(filepath: str) -> str:
    """Read file content from disk.

    Args:
        filepath (str): Path to the file.

    Returns:
        str: File content.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        sys.exit(1)


def main():
    """CLI entry point."""

    if len(sys.argv) < 2:
        print("Usage: python cli_client.py <file.py>")
        sys.exit(1)

    filepath = sys.argv[1]

    code = read_file(filepath)

    client = CLIClient(BACKEND_URL)
    client.send_code(filepath, code)


if __name__ == "__main__":
    main()