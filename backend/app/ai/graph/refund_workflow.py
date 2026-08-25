from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from app.ai.graph.refund_state import RefundState
from app.ai.graph.refund_node import (
    load_order_node,
    load_policy_node,
    check_eligibility_node,
    determine_approval_node,
    human_approval_node,
    create_refund_node,
    rejected_node,
    ineligible_node,
    is_defect_related,
    load_warranty_policy_node,
    check_warranty_eligibility_node,
    warranty_case_node,
    warranty_expired_node,
)


def route_approval_requirement(state: RefundState) -> str:
    if state.get("approval_required"):
        return "human_approval"

    return "create_refund"


def route_human_decision(state: RefundState) -> str:
    if state.get("approved"):
        return "create_refund"

    return "rejected"


def route_after_return_check(state: RefundState) -> str:
    if state.get("eligible"):
        return "determine_approval"

    if is_defect_related(state):
        return "load_warranty_policy"

    return "ineligible"


def route_warranty(state: RefundState) -> str:
    if state.get("warranty_eligible"):
        return "warranty_case"

    return "warranty_expired"


builder = StateGraph(RefundState)


# -------------------------
# Nodes
# -------------------------

builder.add_node(
    "load_order",
    load_order_node,
)

builder.add_node(
    "load_policy",
    load_policy_node,
)

builder.add_node(
    "check_eligibility",
    check_eligibility_node,
)

builder.add_node(
    "determine_approval",
    determine_approval_node,
)

builder.add_node(
    "human_approval",
    human_approval_node,
)

builder.add_node(
    "create_refund",
    create_refund_node,
)

builder.add_node(
    "rejected",
    rejected_node,
)

builder.add_node(
    "ineligible",
    ineligible_node,
)

builder.add_node(
    "load_warranty_policy",
    load_warranty_policy_node,
)

builder.add_node(
    "check_warranty_eligibility",
    check_warranty_eligibility_node,
)

builder.add_node(
    "warranty_case",
    warranty_case_node,
)

builder.add_node(
    "warranty_expired",
    warranty_expired_node,
)


# -------------------------
# Main flow
# -------------------------

builder.add_edge(
    START,
    "load_order",
)

builder.add_edge(
    "load_order",
    "load_policy",
)

builder.add_edge(
    "load_policy",
    "check_eligibility",
)


# -------------------------
# Return eligibility routing
# -------------------------

builder.add_conditional_edges(
    "check_eligibility",
    route_after_return_check,
    {
        "determine_approval": "determine_approval",
        "load_warranty_policy": "load_warranty_policy",
        "ineligible": "ineligible",
    },
)


# -------------------------
# Refund approval routing
# -------------------------

builder.add_conditional_edges(
    "determine_approval",
    route_approval_requirement,
    {
        "human_approval": "human_approval",
        "create_refund": "create_refund",
    },
)

builder.add_conditional_edges(
    "human_approval",
    route_human_decision,
    {
        "create_refund": "create_refund",
        "rejected": "rejected",
    },
)


# -------------------------
# Warranty flow
# -------------------------

builder.add_edge(
    "load_warranty_policy",
    "check_warranty_eligibility",
)

builder.add_conditional_edges(
    "check_warranty_eligibility",
    route_warranty,
    {
        "warranty_case": "warranty_case",
        "warranty_expired": "warranty_expired",
    },
)


# -------------------------
# Terminal nodes
# -------------------------

builder.add_edge(
    "create_refund",
    END,
)

builder.add_edge(
    "rejected",
    END,
)

builder.add_edge(
    "ineligible",
    END,
)

builder.add_edge(
    "warranty_case",
    END,
)

builder.add_edge(
    "warranty_expired",
    END,
)


# -------------------------
# Persistence
# -------------------------

checkpointer = InMemorySaver()

refund_graph = builder.compile(
    checkpointer=checkpointer
)