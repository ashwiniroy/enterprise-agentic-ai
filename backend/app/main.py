from fastapi import FastAPI

from app.ai.observability.tracing import configure_tracing
from app.api.router import api_router
from app.core.config import settings


configure_tracing()


app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
)


app.include_router(
    api_router,
    prefix="/api",
)


@app.get("/")
def root():
    return {
        "message": "Enterprise Agentic AI API",
        "docs": "/docs",
    }