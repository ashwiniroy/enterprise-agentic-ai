from  app.ai.graph.refund_node  import  create_refund
def create_refund_node(state):
    result = create_refund(
        order_id=state["order_id"],
        amount=state["refund_amount"],
        reason=state["reason"],
    )

    return {
        "refund_id": result["refund_id"],
        "status": result["status"],
        "message":
            f"Refund {result['refund_id']} "
            f"was created successfully.",
    }