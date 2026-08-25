from fastapi import APIRouter

from app.ai.models.chat_model import get_chat_model
from app.schemas.chat import ChatRequest, ChatResponse


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    model = get_chat_model()

    result = model.invoke(request.message)

    return ChatResponse(
        response=str(result.content)
    )