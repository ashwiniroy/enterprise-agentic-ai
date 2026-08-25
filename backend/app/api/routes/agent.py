from fastapi import APIRouter, HTTPException
from langchain_core.messages import HumanMessage
from langchain_openai.chat_models.base import (
    OpenAIInvalidRequestError,
)

from app.ai.graph.workflow import agent_graph
from app.ai.guardrails.guardrail_service import (
    guardrail_service,
)
from app.schemas.agent import (
    AgentRequest,
    AgentResponse,
)


router = APIRouter()


@router.post(
    "/agent/chat",
    response_model=AgentResponse,
)
async def agent_chat(
    request: AgentRequest,
):
    input_check = guardrail_service.check_input(
        request.message
    )

    if not input_check.allowed:
        raise HTTPException(
            status_code=400,
            detail=input_check.reason,
        )

    try:
        result =  await agent_graph.ainvoke(
            {
                "messages": [
                    HumanMessage(
                        content=request.message
                    )
                ]
            }
        )

    except OpenAIInvalidRequestError as error:
        error_text = str(error).lower()

        if (
            "content_filter" in error_text
            or "responsibleaipolicyviolation" in error_text
            or "jailbreak" in error_text
        ):
            return AgentResponse(
                response=(
                    "I can't process that request because "
                    "it triggered the application's safety policy."
                )
            )

        raise HTTPException(
            status_code=502,
            detail="The AI provider rejected the request.",
        )

    final_message = result["messages"][-1]

    response_text = str(
        final_message.content
    )

    output_check = guardrail_service.check_output(
        response_text
    )

    return AgentResponse(
        response=output_check.output
    )