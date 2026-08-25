from app.ai.rag.pipeline import ask_rag


def evaluate_rag_case(case: dict) -> dict:
    result = ask_rag(
        case["input"]
    )

    answer = result["answer"].lower()

    expected_values = [
        value.lower()
        for value in case.get(
            "expected_contains",
            []
        )
    ]

    answer_match = all(
        value in answer
        for value in expected_values
    )

    expected_source = case.get(
        "expected_source"
    )

    source_match = True

    if expected_source:
        source_match = any(
            source.get("file_name")
            == expected_source

            for source in result.get(
                "sources",
                []
            )
        )

    passed = (
        answer_match
        and source_match
    )

    return {
        "id": case["id"],
        "type": "rag",
        "passed": passed,
        "answer_match": answer_match,
        "source_match": source_match,
        "answer": result["answer"],
        "sources": result["sources"],
    }