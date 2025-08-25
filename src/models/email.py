from dataclasses import dataclass


@dataclass
class Email:
    address: str
    is_valid: bool
