import flet as ft

from src.models.email import Email


def main(page: ft.Page):
    page.title = "Email Validation"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 300

    email_input = ft.TextField(label="Email", hint_text="Enter your email address")
    email = Email(address=email_input.value, is_valid=False)

    def validate_email(e):
        email.address = email_input.value
        email.is_valid = "@" in email.address and "." in email.address
        email_input.helper = None if email.is_valid else "Invalid email"
        email_input.update()

    page.add(email_input)
    page.add(ft.ElevatedButton("Submit", on_click=validate_email))

    page.update()
