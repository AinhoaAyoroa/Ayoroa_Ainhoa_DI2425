import flet as ft
# TODO PARTE LÓGICA
class CalcButton(ft.ElevatedButton):
    def __init__(self, text, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand

class DigitButton(CalcButton):
    def __init__(self, text, expand=1):
        super().__init__(text, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE

class ActionButton(CalcButton):
    def __init__(self, text, expand=1):
        super().__init__(text, expand)
        self.bgcolor = ft.colors.BLUE_300
        self.color = ft.colors.WHITE

class ExtraActionButton(CalcButton):
    def __init__(self, text, expand=1):
        super().__init__(text, expand)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

def main(page:ft.Page):
    page.title = "Calculadora"
    page.update()

    def resized(e):
        for column in 

    result = ft.Text(value=0, color=ft.colors.WHITE, size=20)

    page.on_resized = resized
    page.add( 
    ft.Container(
        width=350,
        bgcolor=ft.colors.BLACK,
        border_radius=ft.border_radius.all(20),
        padding=20,
        content=ft.Column(
            controls=[
                ft.Row(controls=[result], alignment="end"),
                ft.Divider(),
                ft.Row(controls=[
                            ExtraActionButton(text="AC"),
                            ExtraActionButton(text="+/-"),
                            ExtraActionButton(text="%"),
                            ActionButton(text="/"),

                ]),
                ft.Row(controls=[
                            DigitButton(text="7"),
                            DigitButton(text="8"),
                            DigitButton(text="9"),
                            ActionButton(text="*")

                ]),
                ft.Row(controls=[
                        DigitButton(text="4"),
                        DigitButton(text="5"),
                        DigitButton(text="6"),
                        ActionButton(text="-"),
                ]),
                ft.Row(controls=[
                        DigitButton(text="1"),
                        DigitButton(text="2"),
                        DigitButton(text="3"),
                        ActionButton(text="+"),

                ]),
                ft.Row(controls=[
                        DigitButton(text="0", expand=2),
                        DigitButton(text="."),
                        ActionButton(text="="),

                ]),
            ]
        ) 
    )
)

ft.app(target=main)