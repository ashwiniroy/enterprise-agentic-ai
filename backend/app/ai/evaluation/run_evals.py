import json
from pathlib import Path

from app.ai.evaluation.rag_evaluator import (
    evaluate_rag_case,
)

from app.ai.evaluation.agent_evaluator import (
    evaluate_agent_case,
)

from app.ai.evaluation.workflow_evaluator import (
    evaluate_refund_case,
)


DATASET_PATH = (
    Path(__file__).parent
    / "dataset.json"
)


def load_dataset():
    with open(
        DATASET_PATH,
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


def run_evaluations():

    dataset = load_dataset()

    results = []

    for case in dataset:

        print(
            f"\nRunning {case['id']}..."
        )

        try:

            if case["type"] == "rag":

                result = (
                    evaluate_rag_case(
                        case
                    )
                )

            elif case["type"] == "agent":

                result = (
                    evaluate_agent_case(
                        case
                    )
                )

            elif (
                case["type"]
                == "refund_workflow"
            ):

                result = (
                    evaluate_refund_case(
                        case
                    )
                )

            else:

                print(
                    f"Unknown type: "
                    f"{case['type']}"
                )

                continue

            results.append(
                result
            )

            status = (
                "PASS"
                if result["passed"]
                else "FAIL"
            )

            print(
                f"{case['id']} → "
                f"{status}"
            )

        except Exception as error:

            results.append(
                {
                    "id":
                        case["id"],

                    "passed":
                        False,

                    "error":
                        str(error),
                }
            )

            print(
                f"{case['id']} → ERROR"
            )

            print(error)

    print(
        "\n======================"
    )

    print(
        "EVALUATION SUMMARY"
    )

    print(
        "======================"
    )

    total = len(results)

    passed = sum(
        1
        for result in results
        if result.get("passed")
    )

    failed = (
        total - passed
    )

    print(
        f"Total:  {total}"
    )

    print(
        f"Passed: {passed}"
    )

    print(
        f"Failed: {failed}"
    )

    if total:

        score = (
            passed
            / total
            * 100
        )

        print(
            f"Score:  "
            f"{score:.2f}%"
        )

    return results


if __name__ == "__main__":
    run_evaluations()