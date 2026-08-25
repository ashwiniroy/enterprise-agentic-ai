import json
from pathlib import Path

from langchain_core.messages import HumanMessage

from app.ai.graph.workflow import agent_graph
from app.ai.rag.pipeline import ask_rag


EVALUATION_ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = EVALUATION_ROOT / "dataset.json"

OUTPUT_FILE = (
    Path(__file__).parent
    / "foundry_dataset.jsonl"
)


def prepare_rag_case(case: dict) -> dict:
    result = ask_rag(
        case["input"]
    )

    context = "\n".join(
        str(source)
        for source in result.get(
            "sources",
            []
        )
    )

    ground_truth = " ".join(
        case.get(
            "expected_contains",
            []
        )
    )

    return {
        "case_id": case["id"],
        "case_type": case["type"],
        "query": case["input"],
        "response": result["answer"],
        "context": context,
        "ground_truth": ground_truth,
    }


def prepare_agent_case(case: dict) -> dict:
    result = agent_graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=case["input"]
                )
            ]
        }
    )

    response = str(
        result["messages"][-1].content
    )

    return {
        "case_id": case["id"],
        "case_type": case["type"],
        "query": case["input"],
        "response": response,
        "ground_truth": " ".join(
            case.get(
                "expected_contains",
                []
            )
        ),
        "expected_tool": case.get(
            "expected_tool"
        ),
    }


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Evaluation dataset not found: {INPUT_FILE}"
        )

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8",
    ) as file:
        dataset = json.load(file)

    rows = []

    for case in dataset:
        case_type = case.get("type")

        if case_type == "rag":
            rows.append(
                prepare_rag_case(case)
            )

        elif case_type == "agent":
            rows.append(
                prepare_agent_case(case)
            )

        # Keep refund workflow tests local for now.
        elif case_type == "refund_workflow":
            continue

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8",
    ) as file:
        for row in rows:
            file.write(
                json.dumps(
                    row,
                    ensure_ascii=False,
                )
                + "\n"
            )

    print(
        "\nFoundry dataset created successfully."
    )

    print(
        "Input:",
        INPUT_FILE,
    )

    print(
        "Output:",
        OUTPUT_FILE,
    )

    print(
        "Rows:",
        len(rows),
    )


if __name__ == "__main__":
    main()