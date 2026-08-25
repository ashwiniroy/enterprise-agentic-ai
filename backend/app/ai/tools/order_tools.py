import json

from langchain.tools import tool

from app.services.order_service import (
    get_order_details,
)


@tool
def lookup_order(
    order_id: str,
) -> str:
    """
    Retrieve live transactional information
    for a specific customer order.

    Use this tool when the user provides an
    order ID or asks about:

    - order status
    - ordered product
    - order amount
    - order date
    - delivery date
    - whether a particular order may still
      be eligible for a return

    Do not use this tool for general refund,
    warranty, or return-policy questions.
    """

    order = get_order_details(
        order_id
    )

    if not order:
        return (
            f"No order was found "
            f"with ID {order_id}."
        )

    return json.dumps(
        order,
        indent=2,
    )