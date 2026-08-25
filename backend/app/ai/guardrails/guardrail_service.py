from app.ai.guardrails.input_guardrail import (
    validate_input,
)
from app.ai.guardrails.output_guardrail import (
    validate_output,
)


class GuardrailService:

    @staticmethod
    def check_input(message: str):
        return validate_input(message)

    @staticmethod
    def check_output(response: str):
        return validate_output(response)


guardrail_service = GuardrailService()