import flet as ft


def main(page: ft.Page):
    page.title = "Email Validation"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 400
    page.window.height = 300

    page.add(ft.TextField(label="Email", hint_text="Enter your email"))
    page.add(ft.ElevatedButton("Submit"))

    page.update()
