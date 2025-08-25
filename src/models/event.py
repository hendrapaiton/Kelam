from dataclasses import dataclass
from enum import Enum


class AppEvent(Enum):
    VALIDATE_EMAIL = "validate_email"


@dataclass
class Event:
    type: AppEvent
    payload: dict
