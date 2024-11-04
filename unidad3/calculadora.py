import flet as ft

def main(pagina: ft.Page):
    pagina.title = "Calculadora"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # FUNCIONES BOTONES PARA AGREGAR NÚMEROS Y OPERADORES A LA PANTALLA
    def click_boton1(evento):
        pantalla.value += "1"
        pantalla.update()

    def click_boton2(evento):
        pantalla.value += "2"
        pantalla.update()

    def click_boton3(evento):
        pantalla.value += "3"
        pantalla.update()

    def click_boton4(evento):
        pantalla.value += "4"
        pantalla.update()

    def click_boton5(evento):
        pantalla.value += "5"
        pantalla.update()

    def click_boton6(evento):
        pantalla.value += "6"
        pantalla.update()

    def click_boton7(evento):
        pantalla.value += "7"
        pantalla.update()

    def click_boton8(evento):
        pantalla.value += "8"
        pantalla.update()

    def click_boton9(evento):
        pantalla.value += "9"
        pantalla.update()

    def click_dividir(evento):
        pantalla.value += "/"
        pantalla.update()

    def click_multiplicar(evento):
        pantalla.value += "*"
        pantalla.update()

    def click_restar(evento):
        pantalla.value += "-"
        pantalla.update()

    def click_sumar(evento):
        pantalla.value += "+"
        pantalla.update()


    pantalla = ft.TextField(
        read_only=True,
        bgcolor=ft.colors.WHITE,
        expand=True
    )
    
    # BOTONES DE NÚMERICOS Y CONTADORES
    boton1 = ft.Container(content=ft.Text("1"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREY_200, width=60, height=60, border_radius=8, ink=True, on_click=click_boton1)
    boton2 = ft.Container(content=ft.Text("2"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREY_200, width=60, height=60, border_radius=8, ink=True, on_click=click_boton2)
    boton3 = ft.Container(content=ft.Text("3"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREY_200, width=60, height=60, border_radius=8, ink=True, on_click=click_boton3)
    boton4 = ft.Container(content=ft.Text("4"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREY_200, width=60, height=60, border_radius=8, ink=True, on_click=click_boton4)
    boton5 = ft.Container(content=ft.Text("5"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREY_200, width=60, height=60, border_radius=8, ink=True, on_click=click_boton5)
    boton6 = ft.Container(content=ft.Text("6"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREY_200, width=60, height=60, border_radius=8, ink=True, on_click=click_boton6)
    boton7 = ft.Container(content=ft.Text("7"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREY_200, width=60, height=60, border_radius=8, ink=True, on_click=click_boton7)
    boton8 = ft.Container(content=ft.Text("8"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREY_200, width=60, height=60, border_radius=8, ink=True, on_click=click_boton8)
    boton9 = ft.Container(content=ft.Text("9"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREY_200, width=60, height=60, border_radius=8, ink=True, on_click=click_boton9)

    # BOTONES OPERACIONES
    boton_dividir = ft.Container(content=ft.Text("/"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREEN_200, width=60, height=60, border_radius=8, ink=True, on_click=click_dividir)
    boton_multiplicar = ft.Container(content=ft.Text("*"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREEN_200, width=60, height=60, border_radius=8, ink=True, on_click=click_multiplicar)
    boton_restar = ft.Container(content=ft.Text("-"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREEN_200, width=60, height=60, border_radius=8, ink=True, on_click=click_restar)
    boton_sumar = ft.Container(content=ft.Text("+"), margin=5, alignment=ft.alignment.center, bgcolor=ft.colors.GREEN_200, width=60, height=60, border_radius=8, ink=True, on_click=click_sumar)

    layout_calculadora = ft.Column(
        [
            ft.Row([pantalla]),
            ft.Row([boton7, boton8, boton9, boton_dividir], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([boton4, boton5, boton6, boton_multiplicar], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([boton1, boton2, boton3, boton_restar], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([boton_sumar], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ]
    )
    
    contenedor_principal = ft.Container(
        content=layout_calculadora,
        margin=8,
        padding=8,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.GREY_400,
        width=350,
        height=500,
        border_radius=8,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=10, color=ft.colors.GREEN_200)
    )
    
    pagina.add(contenedor_principal)

ft.app(target=main)
