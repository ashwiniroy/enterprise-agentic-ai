import uuid

from sqlalchemy import text

from app.database.connection import engine


def create_refund(
    order_id: str,
    amount: float,
    reason: str,
):
    refund_id = f"REF-{uuid.uuid4().hex[:8].upper()}"

    query = text(
        """
        INSERT INTO refunds (
            refund_id,
            order_id,
            amount,
            status,
            reason
        )
        VALUES (
            :refund_id,
            :order_id,
            :amount,
            :status,
            :reason
        )
        """
    )

    with engine.begin() as connection:
        connection.execute(
            query,
            {
                "refund_id": refund_id,
                "order_id": order_id,
                "amount": amount,
                "status": "CREATED",
                "reason": reason,
            },
        )

    return {
        "refund_id": refund_id,
        "status": "CREATED",
    }