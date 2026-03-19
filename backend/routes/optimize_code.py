"""Route responsible for optimizing Python code using the AI service."""

import traceback
import logging

from fastapi import APIRouter, HTTPException
from backend.models.request_models import CodeRequest
from services.linter_service import LinterService
from services.ai_service import DeepSeekClient

router = APIRouter()

linter = LinterService()
ai_client = DeepSeekClient()

logger = logging.getLogger(__name__)

@router.post("/optimize-code")
def optimize_code(request: CodeRequest):
    """Receive Python code and return a placeholder optimization response.

    Args:
        request (CodeRequest): Incoming request containing the code.

    Returns:
        dict: Placeholder response for code optimization.
    """

    try:
        logger.info(f"Processing file: {request.filename}")
        # 1. Linter Analyse
        lint_result = linter.analyze(request.code)

        # 2. Falls Fehler
        if lint_result["has_errors"]:
            logger.info(f"Processing file: {request.filename}")

            optimized_code = ai_client.optimize_code(request.code)

            return {
                "filename": request.filename,
                "optimized": True,
                "lint_errors": lint_result["errors"],
                "code": optimized_code
            }
        
        logger.info("No lint errors found")
        # 3. Kein Fehler
        return {
            "filename": request.filename,
            "optimized": False,
            "lint_errors": [],
            "code": request.code
        }

    except Exception as e:
        logger.error("Error during optimization")
        logger.error(traceback.format_exc())
        
        # Traceback in der Konsole ausgeben
        traceback.print_exc()
        # HTTP 500 mit Fehlertext zurückgeben
        raise HTTPException(status_code=500, detail=str(e))