import flet as ft
from src.models.email import Email
from src.models.event import Event, AppEvent


def view(model: Email, dispatch):
    return ft.Column(
        controls=[
            ft.TextField(
                label="Email",
                value=model.address,
                hint_text="Enter your email address",
                on_change=lambda e: dispatch(
                    Event(AppEvent.VALIDATE_EMAIL, {"value": e.control.value})
                ),
                autofocus=True,
            ),
            ft.Text(
                value="Email Valid" if model.is_valid else "Email Invalid",
                color="green" if model.is_valid else "red"
            )
        ]
    )
