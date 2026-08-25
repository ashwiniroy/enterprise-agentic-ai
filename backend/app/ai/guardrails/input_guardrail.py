from dataclasses import dataclass

from app.ai.guardrails.pii_guardrail import (
    detect_pii,
)
from app.ai.guardrails.prompt_injection_guardrail import (
    detect_prompt_injection,
)


@dataclass
class InputGuardrailResult:
    allowed: bool
    reason: str | None = None


MAX_INPUT_LENGTH = 4000


def validate_input(
    message: str,
) -> InputGuardrailResult:

    if not message.strip():
        return InputGuardrailResult(
            allowed=False,
            reason="Message cannot be empty.",
        )

    if len(message) > MAX_INPUT_LENGTH:
        return InputGuardrailResult(
            allowed=False,
            reason="Message is too long.",
        )

    if detect_prompt_injection(message):
        return InputGuardrailResult(
            allowed=False,
            reason=(
                "The request contains instructions "
                "that attempt to override the "
                "assistant's system rules."
            ),
        )

    pii = detect_pii(message)

    if pii["possible_card_detected"]:
        return InputGuardrailResult(
            allowed=False,
            reason=(
                "Please do not provide full payment "
                "card numbers."
            ),
        )

    return InputGuardrailResult(
        allowed=True
    )