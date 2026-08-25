from langgraph.graph import (
    StateGraph,
    START,
)

from langgraph.prebuilt import (
    ToolNode,
    tools_condition,
)

from app.ai.agents.supervisor_agent import (
    supervisor_agent,
    tools,
)

from app.ai.graph.state import AgentState


tool_node = ToolNode(
    tools,
    handle_tool_errors=True,
)


builder = StateGraph(
    AgentState
)


builder.add_node(
    "supervisor",
    supervisor_agent,
)


builder.add_node(
    "tools",
    tool_node,
)


builder.add_edge(
    START,
    "supervisor",
)


builder.add_conditional_edges(
    "supervisor",
    tools_condition,
)


builder.add_edge(
    "tools",
    "supervisor",
)


agent_graph = builder.compile()