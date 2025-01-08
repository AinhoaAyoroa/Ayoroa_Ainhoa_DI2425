import flet as ft

def main(page):
    def button_clicked(e):
        text.value = f"Your favorite color is:  {radioGroup.value}"
        page.update()

    def button_changed(e):
        button.disabled=False
        button.update()

    text = ft.Text()
    button = ft.ElevatedButton(text='Submit', on_click=button_clicked, disabled=True)
    radioGroup = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="red", label="Red"),
        ft.Radio(value="green", label="Green"),
        ft.Radio(value="blue", label="Blue")]
        ), on_change=button_changed)
    page.add(ft.Text("Select your favorite color:"), radioGroup, button, text)

ft.app(target=main)