import re
from src.models.email import Email
from src.models.event import Event, AppEvent


def update(model: Email, event: Event) -> Email:
    if event.type == AppEvent.VALIDATE_EMAIL:
        address = event.payload.get("value", "")
        model.address = address
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", address):
            model.is_valid = True
        else:
            model.is_valid = False
    return model
