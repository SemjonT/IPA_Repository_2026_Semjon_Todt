"""Route responsible for optimizing Python code using the AI service."""

from fastapi import APIRouter
from backend.models.request_models import CodeRequest
from services.linter_service import LinterService
from services.ai_service import DeepSeekClient

router = APIRouter()

linter = LinterService()
ai_client = DeepSeekClient()

@router.post("/optimize-code")
def optimize_code(request: CodeRequest):
    """Receive Python code and return a placeholder optimization response.

    Args:
        request (CodeRequest): Incoming request containing the code.

    Returns:
        dict: Placeholder response for code optimization.
    """

    # 1. Linter Analyse
    lint_result = linter.analyze(request.code)

    # 2. Falls Fehler
    if lint_result["has_errors"]:
        optimized_code = ai_client.optimize_code(request.code)

        return {
            "filename": request.filename,
            "optimized": True,
            "lint_errors": lint_result["errors"],
            "code": optimized_code
        }

    # 3. Kein Fehler
    return {
        "filename": request.filename,
        "optimized": False,
        "lint_errors": [],
        "code": request.code
    }