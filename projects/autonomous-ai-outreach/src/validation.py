from .models import OutreachMessage


SUPPORTED_CHANNELS = {"linkedin", "x", "email"}


def validate_message(message: OutreachMessage) -> tuple[bool, list[str]]:
    errors = []

    if message.channel.lower() not in SUPPORTED_CHANNELS:
        errors.append(f"Unsupported channel: {message.channel}")

    if not message.message.strip():
        errors.append("Message cannot be empty.")

    if not 0 <= message.confidence <= 1:
        errors.append("Confidence must be between 0 and 1.")

    if not message.reasoning.strip():
        errors.append("Reasoning cannot be empty.")

    return len(errors) == 0, errors
