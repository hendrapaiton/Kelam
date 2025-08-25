import flet as ft

from src.models.email import Email
from src.views.email_form import view
from src.views.email_dispatcher import make_dispatch


def main(page: ft.Page):
    page.title = "Email Validation"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 300

    model = Email()
    ui_container = None

    def render():
        nonlocal ui_container
        if ui_container is None:
            ui_container = view(model, dispatch)
            page.controls.clear()
            page.add(ui_container)
            page.update()
            return

        try:
            validity_text = ui_container.controls[1]
            validity_text.value = "Email Valid" if model.is_valid else "Email Invalid"
            validity_text.color = "green" if model.is_valid else "red"
        except Exception:
            page.controls.clear()
            ui_container = view(model, dispatch)
            page.add(ui_container)

        page.update()

    dispatch = make_dispatch(model, render)
    render()
