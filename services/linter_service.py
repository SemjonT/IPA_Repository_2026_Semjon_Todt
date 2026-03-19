"""Service responsible for performing Python code linting."""

import subprocess
import tempfile
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class LinterService:
    """Service for analyzing Python code using flake8."""

    def analyze(self, code: str) -> Dict[str, object]:
        """Analyze Python code for PEP8 violations.

        Args:
            code (str): Python source code.

        Returns:
            dict: Linter result containing errors and status.
        """
        try:

            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".py", delete=True
            ) as temp_file:

                temp_file.write(code)
                temp_file.flush()

                result = subprocess.run(
                    ["python3", "-m", "flake8", temp_file.name],
                    capture_output=True,
                    text=True
                )

                errors = (
                    result.stdout.strip().split("\n")
                    if result.stdout else []
                )

            return {
                "has_errors": len(errors) > 0,
                "errors": errors
            }
        
        except Exception as e:
            logger.error("Linter failed")
            logger.error(str(e))

            return {
                "has_errors": True,
                "errors": ["Linter execution failed"]
            }