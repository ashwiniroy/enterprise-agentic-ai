from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.chat import router as chat_router
from app.api.routes.rag import router as rag_router
from app.api.routes.agent import (
    router as agent_router,
)
from app.api.routes.refunds import (
    router as refund_router,
)




api_router = APIRouter()

api_router.include_router(
    health_router,
    tags=["Health"],
)

api_router.include_router(
    chat_router,
    tags=["Chat"],
)

api_router.include_router(
    rag_router,
    tags=["RAG"],
)


api_router.include_router(
    agent_router,
    tags=["Agentic AI"],
)

api_router.include_router(
    refund_router,
    tags=["Refunds"],
)