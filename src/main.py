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

    def render():
        page.controls.clear()
        page.add(view(model, dispatch))
        page.update()

    dispatch = make_dispatch(model, render)
    render()
