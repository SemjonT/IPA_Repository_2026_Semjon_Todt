"""Data models used for API requests."""

from pydantic import BaseModel


class CodeRequest(BaseModel):
    """Model representing a code analysis or optimization request.

    Args:
        filename (str): Name of the Python file.
        code (str): Source code to analyze or optimize.

    Returns:
        CodeRequest: Structured request object.
    """

    filename: str
    code: str