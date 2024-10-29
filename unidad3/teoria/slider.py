import flet as ft

def main(page):

    def slider_changed(e):
        texto.value = f"Slider changed to {round(e.control.value)}"
        page.update()

    texto = ft.Text()
    page.add(
        ft.Text("Slider with 'on_change' event:"),
        ft.Slider(min=0, max=100, divisions=10000, label="{value}%", on_change=slider_changed), texto)

ft.app(target=main)