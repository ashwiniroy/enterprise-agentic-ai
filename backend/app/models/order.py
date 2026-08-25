from sqlalchemy import (
    Column,
    Date,
    Numeric,
    String,
)

from app.database.base import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(
        String(50),
        primary_key=True,
    )

    customer_name = Column(
        String(100),
        nullable=False,
    )

    product_name = Column(
        String(200),
        nullable=False,
    )

    product_id = Column(
        String(50),
    )

    order_date = Column(
        Date,
        nullable=False,
    )

    delivery_date = Column(
        Date,
    )

    amount = Column(
        Numeric(10, 2),
    )

    status = Column(
        String(50),
        nullable=False,
    )