from langchain_core.messages import SystemMessage

from app.ai.models.chat_model import get_chat_model
from app.ai.prompts.supervisor_prompt import (
    SUPERVISOR_SYSTEM_PROMPT,
)
from app.ai.tools.rag_tools import (
    search_knowledge_base,
)
from app.ai.tools.order_tools import (
    lookup_order,
)
from app.ai.tools.eligibility_tool import (
    check_return_eligibility,
)
from app.ai.tools.refund_tools import (
    start_refund_request,
)


tools = [
    search_knowledge_base,
    lookup_order,
    check_return_eligibility,
    start_refund_request,
]


# Local evaluation/debug tracking only.
# Do not use this global approach in production with concurrent requests.
LAST_TOOL_CALLS = []


model = get_chat_model()

model_with_tools = model.bind_tools(
    tools
)


async def supervisor_agent(state):
    global LAST_TOOL_CALLS

    messages = state["messages"]

    response =  await model_with_tools.ainvoke(
        [
            SystemMessage(
                content=SUPERVISOR_SYSTEM_PROMPT
            ),
            *messages,
        ]
    )

    current_tool_calls = [
        tool_call["name"]
        for tool_call in response.tool_calls
    ]

    # Important:
    # accumulate tool calls across multiple supervisor executions
    # instead of replacing the previous list.
    LAST_TOOL_CALLS.extend(
        current_tool_calls
    )

    print(
        "\n===== SUPERVISOR RESPONSE ====="
    )

    print(
        "Content:",
        response.content,
    )

    print(
        "Current tool calls:",
        current_tool_calls,
    )

    print(
        "All tool calls for this evaluation:",
        LAST_TOOL_CALLS,
    )

    return {
        "messages": [response]
    }