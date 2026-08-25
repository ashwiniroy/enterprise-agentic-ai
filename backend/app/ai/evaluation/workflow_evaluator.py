import uuid

from app.ai.graph.refund_workflow import (
    refund_graph,
)


def evaluate_refund_case(
    case: dict,
) -> dict:

    thread_id = (
        f"eval-{uuid.uuid4()}"
    )

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    result = refund_graph.invoke(
        {
            "order_id":
                case["order_id"],

            "reason":
                case["reason"],
        },
        config=config,
    )

    expected_interrupt = case.get(
        "expected_interrupt",
        False,
    )

    # LangGraph may expose interrupts
    # using __interrupt__.
    interrupted = bool(
        result.get("__interrupt__")
    )

    if expected_interrupt:
        passed = interrupted

        return {
            "id": case["id"],
            "type":
                "refund_workflow",
            "passed": passed,
            "expected_interrupt":
                True,
            "actual_interrupt":
                interrupted,
            "result": result,
        }

    expected_status = case.get(
        "expected_status"
    )

    actual_status = result.get(
        "status"
    )

    passed = (
        actual_status
        == expected_status
    )

    return {
        "id": case["id"],
        "type":
            "refund_workflow",
        "passed": passed,
        "expected_status":
            expected_status,
        "actual_status":
            actual_status,
        "result":
            result,
    }