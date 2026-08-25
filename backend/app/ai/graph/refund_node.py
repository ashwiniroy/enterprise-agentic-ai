from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from langgraph.types import interrupt

from app.ai.rag.retriever import retrieve_documents
from app.repositories.refund_repository import create_refund
from app.services.order_service import get_order_details


def load_order_node(state):
    order_id = state["order_id"]

    order = get_order_details(order_id)

    if not order:
        return {
            "status": "ORDER_NOT_FOUND",
            "message": f"Order {order_id} was not found.",
        }

    return {
        "product_name": order["product_name"],
        "delivery_date": order["delivery_date"],
        "order_amount": order["amount"],

        # Refund amount comes from trusted order data
        "refund_amount": order["amount"],
    }


def warranty_case_node(state):
    return {
        "status": "WARRANTY_ELIGIBLE",
        "message": (
            f"The standard return window has expired, "
            f"but {state['product_name']} is still within "
            f"its {state['warranty_months']}-month warranty. "
            f"A warranty support case should be created."
        ),
    }


def warranty_expired_node(state):
    return {
        "status": "WARRANTY_EXPIRED",
        "message": (
            "The standard return window has expired "
            "and the product is no longer within warranty."
        ),
    }


def is_defect_related(state) -> bool:
    reason = state.get("reason", "").lower()

    defect_keywords = [
        "defect",
        "defective",
        "broken",
        "faulty",
        "malfunction",
        "malfunctioning",
        "not working",
        "stopped working",
        "doesn't work",
        "does not work",
    ]

    return any(
        keyword in reason
        for keyword in defect_keywords
    )


def load_policy_node(state):
    product_name = state["product_name"]

    documents = retrieve_documents(
        f"{product_name} return window days",
        k=3,
    )

    # Temporary deterministic mapping for our sample dataset.
    # We will replace this later with structured extraction.
    return_window_days = 30

    if "iPhone 16" in product_name:
        return_window_days = 14

    elif "Samsung 55-inch OLED TV" in product_name:
        return_window_days = 15

    return {
        "return_window_days": return_window_days,
    }


def load_warranty_policy_node(state):
    product_name = state["product_name"]

    documents = retrieve_documents(
        f"{product_name} warranty months",
        k=3,
    )

    # Temporary deterministic extraction
    # from our known sample product catalog.
    warranty_months = 12

    if "Samsung 55-inch OLED TV" in product_name:
        warranty_months = 24

    elif "OfficePro Ergonomic Chair" in product_name:
        warranty_months = 24

    return {
        "warranty_months": warranty_months
    }


def check_warranty_eligibility_node(state):
    delivery_date = state.get("delivery_date")

    if not delivery_date:
        return {
            "warranty_eligible": False,
            "status": "NO_DELIVERY_DATE",
            "message": (
                "Warranty eligibility could not be determined."
            ),
        }

    delivered = datetime.strptime(
        delivery_date,
        "%Y-%m-%d",
    ).date()

    warranty_months = state["warranty_months"]

    warranty_end_date = (
        delivered
        + relativedelta(
            months=warranty_months
        )
    )

    today = date.today()

    warranty_eligible = (
        delivered <= today <= warranty_end_date
    )

    return {
        "warranty_eligible": warranty_eligible,
        "warranty_end_date": str(warranty_end_date),
        "message": (
            f"Warranty valid until {warranty_end_date}."
        ),
    }


def check_eligibility_node(state):
    delivery_date = state.get("delivery_date")

    if not delivery_date:
        return {
            "eligible": False,
            "status": "NOT_DELIVERED",
            "message": (
                "The order has not been delivered yet."
            ),
        }

    delivered = datetime.strptime(
        delivery_date,
        "%Y-%m-%d",
    ).date()

    today = date.today()

    days_since_delivery = (
        today - delivered
    ).days

    return_window_days = state[
        "return_window_days"
    ]

    eligible = (
        0 <= days_since_delivery <= return_window_days
    )

    remaining_days = max(
        return_window_days - days_since_delivery,
        0,
    )

    return {
        "eligible": eligible,
        "remaining_days": remaining_days,
    }


def determine_approval_node(state):
    refund_amount = state["refund_amount"]

    return {
        "approval_required": refund_amount > 500
    }


def human_approval_node(state):
    approval = interrupt(
        {
            "type": "refund_approval",
            "order_id": state["order_id"],
            "product_name": state["product_name"],
            "order_amount": state["order_amount"],
            "refund_amount": state["refund_amount"],
            "reason": state["reason"],
            "message": (
                "Refund exceeds $500. "
                "Human approval is required."
            ),
        }
    )

    return {
        "approved": bool(approval)
    }


def create_refund_node(state):
    refund_amount = state["refund_amount"]
    order_amount = state["order_amount"]

    if refund_amount > order_amount:
        return {
            "status": "INVALID_AMOUNT",
            "message": (
                "Refund amount cannot exceed "
                "the order amount."
            ),
        }

    result = create_refund(
        order_id=state["order_id"],
        amount=refund_amount,
        reason=state["reason"],
    )

    return {
        "refund_id": result["refund_id"],
        "status": result["status"],
        "message": (
            f"Refund {result['refund_id']} "
            f"for ${refund_amount:.2f} "
            f"was created successfully."
        ),
    }


def rejected_node(state):
    return {
        "status": "REJECTED",
        "message": (
            "The refund request was rejected "
            "by the approver."
        ),
    }


def ineligible_node(state):
    return {
        "status": "INELIGIBLE",
        "message": (
            "The order is outside "
            "the standard return window."
        ),
    }