from typing import TypedDict


class RefundState(TypedDict, total=False):
    order_id: str

    product_name: str
    delivery_date: str
    order_amount: float

    return_window_days: int
    warranty_months: int

    eligible: bool
    warranty_eligible: bool

    remaining_days: int
    refund_amount: float

    reason: str

    approval_required: bool
    approved: bool | None

    refund_id: str
    status: str
    message: str


def is_defect_related(state) -> bool:
    reason = state.get("reason", "").lower()

    defect_keywords = [
        "defect",
        "defective",
        "not working",
        "stopped working",
        "broken",
        "malfunction",
        "faulty",
    ]

    return any(
        keyword in reason
        for keyword in defect_keywords
    )