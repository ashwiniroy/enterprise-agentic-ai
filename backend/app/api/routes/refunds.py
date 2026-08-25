import uuid

from fastapi import APIRouter

from langgraph.types import Command

from app.ai.graph.refund_workflow import (
    refund_graph,
)

from app.schemas.refund import (
    RefundRequest,
    RefundApprovalRequest,
)


router = APIRouter()


@router.post("/refunds")
def request_refund(
    request: RefundRequest,
):
    thread_id = str(
        uuid.uuid4()
    )

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    result = refund_graph.invoke(
        {
            "order_id": request.order_id,
            "reason": request.reason,
        },
        config=config,
    )

    return {
        "thread_id": thread_id,
        "result": result,
    }



@router.post("/refunds/approve")
def approve_refund(
    request: RefundApprovalRequest,
):
    config = {
        "configurable": {
            "thread_id":
                request.thread_id
        }
    }

    result = refund_graph.invoke(
        Command(
            resume=request.approved
        ),
        config=config,
    )

    return result