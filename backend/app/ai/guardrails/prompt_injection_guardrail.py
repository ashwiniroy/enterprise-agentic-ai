SUSPICIOUS_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "reveal system prompt",
    "show system prompt",
    "developer message",
    "bypass safety",
    "disable guardrails",
    "forget your instructions",
]


def detect_prompt_injection(text: str) -> bool:
    normalized = text.lower()

    return any(
        pattern in normalized
        for pattern in SUSPICIOUS_PATTERNS
    )