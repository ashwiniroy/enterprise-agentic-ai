from sqlalchemy import select

from app.database.session import SessionLocal
from app.models.order import Order


def get_order_by_id(
    order_id: str,
) -> Order | None:

    with SessionLocal() as session:

        statement = select(Order).where(
            Order.order_id == order_id
        )

        return session.scalar(statement)