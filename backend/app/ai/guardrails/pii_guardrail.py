import re


EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)

CARD_PATTERN = re.compile(
    r"\b(?:\d[ -]*?){13,19}\b"
)


def detect_pii(text: str) -> dict:
    return {
        "email_detected": bool(
            EMAIL_PATTERN.search(text)
        ),
        "possible_card_detected": bool(
            CARD_PATTERN.search(text)
        ),
    }


def redact_sensitive_data(text: str) -> str:
    text = EMAIL_PATTERN.sub(
        "[REDACTED_EMAIL]",
        text,
    )

    text = CARD_PATTERN.sub(
        "[REDACTED_CARD]",
        text,
    )

    return text