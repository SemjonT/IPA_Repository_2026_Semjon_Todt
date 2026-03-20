"""Data models used for API requests."""

from pydantic import BaseModel


class CodeRequest(BaseModel):
    """Model representing a code analysis or optimization request.

    Attributes:
        filename (str): Name of the Python file.
        code (str): Source code to analyze or optimize.
    """

    filename: str
    code: str
