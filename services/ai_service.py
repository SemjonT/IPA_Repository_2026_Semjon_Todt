"""Service responsible for communication with the DeepSeek API."""

from fileinput import filename
import os
from urllib import response
import requests
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"


class DeepSeekClient:
    """Client responsible for sending requests to the DeepSeek API."""

    def __init__(self):
        """Initialize DeepSeek client with API configuration."""
        self.api_key = DEEPSEEK_API_KEY
        self.url = DEEPSEEK_URL

    def optimize_code(self, code: str) -> str:
        """Send Python code to DeepSeek and receive optimized code.

        Args:
            code (str): Python source code to optimize.

        Returns:
            str: Optimized Python code returned by the AI.
        """

        prompt = self._build_prompt(code)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek-chat",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a Python code reviewer. "
                        "Fix PEP8 violations, enforce snake_case naming, "
                        "and add missing Google-style docstrings. "
                        "Return the full corrected Python code only."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        response = requests.post(self.url, headers=headers, json=payload)

        if response.status_code != 200:
            logger.error(f"DeepSeek API error: {response.status_code}")
            logger.error(response.text)
            
            raise Exception(
                f"DeepSeek API error: {response.status_code} {response.text}"
            )
        
        if response.status_code == 401:
            logger.error("Invalid DeepSeek API key.")
            raise Exception("Authentication failed")

        data = response.json()

        optimized_code = data["choices"][0]["message"]["content"]

        return optimized_code

    def _build_prompt(self, code: str) -> str:
        """Generate the prompt for the DeepSeek API.

        Args:
            code (str): Python code to optimize.

        Returns:
            str: Prompt containing the code.
        """

        return f"Optimize the following Python code from the {filename} file:\n\n{code}"