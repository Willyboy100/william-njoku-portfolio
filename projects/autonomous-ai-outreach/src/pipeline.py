from .models import Lead, OutreachMessage
from .validation import validate_message


def qualify_lead(lead: Lead) -> bool:
    """
    Simple deterministic qualification gate.

    In a production system, this could combine:
    - ICP rules
    - lead score
    - company attributes
    - enrichment data
    """

    return lead.company_size >= 50 and bool(lead.needs.strip())


def build_message(lead: Lead) -> OutreachMessage:
    """
    Sanitized reference implementation.

    In production, this stage would call an LLM using
    the lead context and channel-specific instructions.
    """

    message = (
        f"Hi {lead.first_name}, I noticed {lead.company} is working "
        f"on {lead.needs}. I'd be interested in learning more about "
        f"how your team approaches this."
    )

    return OutreachMessage(
        channel=lead.channel,
        message=message,
        reasoning="Generated from structured lead context.",
        confidence=0.85,
    )


def run_pipeline(lead: Lead) -> dict:
    """
    Execute the reference outreach pipeline.
    """

    if not qualify_lead(lead):
        return {
            "status": "rejected",
            "reason": "Lead did not pass qualification.",
        }

    message = build_message(lead)

    valid, errors = validate_message(message)

    if not valid:
        return {
            "status": "validation_failed",
            "errors": errors,
        }

    return {
        "status": "ready",
        "channel": message.channel,
        "message": message.message,
        "confidence": message.confidence,
    }
