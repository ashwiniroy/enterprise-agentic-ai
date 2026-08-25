def ineligible_node(state):
    return {
        "status": "INELIGIBLE",
        "message":
            "The order is outside the "
            "standard return window.",
    }