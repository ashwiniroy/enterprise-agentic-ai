from langchain_core.messages import HumanMessage

from app.ai.graph.workflow import agent_graph

import app.ai.agents.supervisor_agent as supervisor_module


def evaluate_agent_case(
    case: dict,
) -> dict:

    supervisor_module.LAST_TOOL_CALLS = []

    result = agent_graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=case["input"]
                )
            ]
        }
    )

    final_message = (
        result["messages"][-1]
    )

    response = str(
        final_message.content
    )

    tool_calls = (
        supervisor_module
        .LAST_TOOL_CALLS
    )

    expected_tool = case.get(
        "expected_tool"
    )

    tool_match = True

    if expected_tool:
        tool_match = (
            expected_tool
            in tool_calls
        )

    expected_values = [
        value.lower()
        for value in case.get(
            "expected_contains",
            []
        )
    ]

    response_match = all(
        value in response.lower()
        for value in expected_values
    )

    return {
        "id": case["id"],
        "type": "agent",
        "passed": (
            tool_match
            and response_match
        ),
        "expected_tool":
            expected_tool,
        "actual_tools":
            tool_calls,
        "tool_match":
            tool_match,
        "response_match":
            response_match,
        "response":
            response,
    }