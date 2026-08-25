from app.ai.rag.retriever import retrieve_documents


def load_policy_node(state):
    product_name = state["product_name"]

    documents = retrieve_documents(
        f"{product_name} return window days",
        k=3,
    )

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    # For now, because our sample dataset is known,
    # we will extract this deterministically where possible.
    #
    # Later we'll use structured LLM output here.

    return_window_days = 30

    if "iPhone 16" in product_name:
        return_window_days = 14

    elif "Samsung 55-inch OLED TV" in product_name:
        return_window_days = 15

    return {
        "return_window_days": return_window_days,
    }