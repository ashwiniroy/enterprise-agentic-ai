from dataclasses import dataclass

from app.ai.guardrails.pii_guardrail import (
    redact_sensitive_data,
)


@dataclass
class OutputGuardrailResult:
    allowed: bool
    output: str
    reason: str | None = None


FORBIDDEN_PATTERNS = [
    "azure_openai_api_key",
    "api key is",
    "database password",
    "connection string is",
]


def validate_output(
    output: str,
) -> OutputGuardrailResult:

    normalized = output.lower()

    for pattern in FORBIDDEN_PATTERNS:
        if pattern in normalized:
            return OutputGuardrailResult(
                allowed=False,
                output=(
                    "I cannot return sensitive "
                    "system credentials."
                ),
                reason=(
                    "Potential secret leakage detected."
                ),
            )

    cleaned_output = redact_sensitive_data(
        output
    )

    return OutputGuardrailResult(
        allowed=True,
        output=cleaned_output,
    )