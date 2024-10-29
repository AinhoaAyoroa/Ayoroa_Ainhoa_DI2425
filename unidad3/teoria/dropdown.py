import flet as ft

def main(page: ft.Page):
    def dropdown_changed(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ], 
        on_change=dropdown_changed
    )
    page.add(color_dropdown, output_text)

ft.app(target=main)