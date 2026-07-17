"""
utils/validators.py
-------------------

Validation utilities for the AI Email Writer.
"""

from config import VALID_LENGTHS, VALID_TONES


def validate_required(value: str, field_name: str) -> None:
    """
    Ensures a required text field is not empty.
    """
    if not value or not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")


def validate_tone(tone: str) -> None:
    """
    Validates the selected email tone.
    """
    if tone not in VALID_TONES:
        raise ValueError(
            f"Invalid tone '{tone}'. "
            f"Choose one of: {', '.join(VALID_TONES)}."
        )


def validate_length(length: str) -> None:
    """
    Validates the selected email length.
    """
    if length not in VALID_LENGTHS:
        raise ValueError(
            f"Invalid length '{length}'. "
            f"Choose one of: {', '.join(VALID_LENGTHS)}."
        )


def validate_generate_email(
    purpose: str,
    recipient: str,
    context: str,
    tone: str,
    length: str,
) -> None:
    """
    Validate all inputs for email generation.
    """
    validate_required(purpose, "Purpose")
    validate_required(recipient, "Recipient")
    validate_required(context, "Context")

    validate_tone(tone)
    validate_length(length)


def validate_rewrite(email: str, instruction: str) -> None:
    validate_required(email, "Email")
    validate_required(instruction, "Instruction")


def validate_grammar(text: str) -> None:
    validate_required(text, "Email")


def validate_subject(text: str) -> None:
    validate_required(text, "Context")