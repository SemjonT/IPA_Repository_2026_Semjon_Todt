"""Health check route for the backend service."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    """Check if the backend service is running.

    Returns:
        dict: Status information of the backend.
    """
    return {"status": "ok"}
