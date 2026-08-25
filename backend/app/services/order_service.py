from app.repositories.order_repository import (
    get_order_by_id,
)


def get_order_details(
    order_id: str,
):

    order = get_order_by_id(
        order_id
    )

    if not order:
        return None

    return {
        "order_id": order.order_id,
        "customer_name": order.customer_name,
        "product_name": order.product_name,
        "product_id": order.product_id,
        "order_date": str(
            order.order_date
        ),
        "delivery_date": (
            str(order.delivery_date)
            if order.delivery_date
            else None
        ),
        "amount": float(
            order.amount
        ),
        "status": order.status,
    }