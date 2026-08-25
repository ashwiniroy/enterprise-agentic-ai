from datetime import date, datetime

from langchain.tools import tool


@tool
def check_return_eligibility(
    delivery_date: str,
    return_window_days: int,
) -> str:
    """
    Calculate whether an order is still within its return window.

    Use this after retrieving an order's delivery date and
    the applicable product return window.
    """

    delivered = datetime.strptime(
        delivery_date,
        "%Y-%m-%d",
    ).date()

    today = date.today()

    days_since_delivery = (
        today - delivered
    ).days

    eligible = (
        0 <= days_since_delivery <= return_window_days
    )

    remaining_days = max(
        return_window_days - days_since_delivery,
        0,
    )

    return (
        f"Delivery date: {delivered}. "
        f"Current date: {today}. "
        f"Days since delivery: {days_since_delivery}. "
        f"Return window: {return_window_days} days. "
        f"Eligible: {eligible}. "
        f"Remaining days: {remaining_days}."
    )