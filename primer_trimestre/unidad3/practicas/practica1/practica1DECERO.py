import flet as ft
import random

def main(page: ft.Page):

    numero = random.randint(1, items)
    acertado = False

    def items(contador):
        items = []
        for i in range(1, contador + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=str(i)),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e, num=i: verificar(num), 
                ),
            )
        return items

    def verificar(num):
        nonlocal acertado
        if num == numero:
            acertado = True
            page.go("/correcto")  
        else:
            page.go("/incorrecto") 

    row = ft.Row(
        wrap=True,
        spacing=5,
        controls=items(25), 
        width=page.window_width,
        )

    
    page.add(row)

ft.app(target=main)
