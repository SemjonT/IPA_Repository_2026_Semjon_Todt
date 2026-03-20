"""Main entry point for the FastAPI backend application."""

from fastapi import FastAPI
from services.logging_config import setup_logging

from backend.routes import health
from backend.routes import optimize_code

setup_logging()

app = FastAPI(
    title="AI Code Optimization API",
    description="Backend service for automated Python code "
    "analysis and optimization.",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(optimize_code.router)
