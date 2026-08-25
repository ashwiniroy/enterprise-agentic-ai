from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

from app.ai.rag.pipeline import ask_rag


router = APIRouter()


class RagRequest(BaseModel):
    question: str


class RagResponse(BaseModel):
    answer: str
    sources: list[dict[str, Any]]

@router.post("/ask")
async def rag_ask(request: RagRequest):
    return await ask_rag(request.question)