import flet as ft
import os

helados = {sabores: "chocolate", "fresa", "nata", "menta"}

def main(page: ft.Page):
    page.title = "Simulador de Comandas - Heladeria"
    page.vertical_alignment = ft.MainAxisAlignment.START

    label_recipients = ll

    page.add(ft.ResponsiveRow(
        controls=[
            ft.Column(
                controls=[
                    ft.Text(list(helados.keys[][0]))
                ]
                col=["": 6, "": 4, "": 3]
            ),
            ft.Column(
                controls=[
                    ft.Text(list(helados.keys[][0]))
                ]
                col=["": 6, "": 4, "": 3]
            ),
            ft.Column(
                controls=[
                    ft.Text(list(helados.keys[][0]))
                ]
                col=["": 6, "": 4, "": 3]
            ),
            ft.Column(
                controls=[
                    ft.Text(list(helados.keys[][0]))
                ]
                col=["": 6, "": 4, "": 3]
            )

        ]


    ))