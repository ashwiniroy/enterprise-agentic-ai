from langchain.tools import tool

from app.ai.graph.refund_workflow import refund_graph


@tool
def start_refund_request(
    order_id: str,
    reason: str,
) -> str:
    """
    Start a refund request for a specific order.

    Use this tool when the user explicitly wants to:
    - request a refund
    - return an order for a refund
    - get money back for an order

    Do not use this tool for general refund-policy questions.
    """

    result = refund_graph.invoke(
        {
            "order_id": order_id,
            "reason": reason,
        },
        config={
            "configurable": {
                "thread_id": f"refund-{order_id}"
            }
        },
    )

    return str(result)