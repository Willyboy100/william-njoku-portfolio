from dataclasses import dataclass
from typing import List


@dataclass
class Lead:
    first_name: str
    company: str
    title: str
    company_size: int
    needs: str
    channel: str


@dataclass
class OutreachMessage:
    channel: str
    message: str
    reasoning: str
    confidence: float
