import flet as ft
import os

class Sabores(ft.Column):
    def __init__(self):
        super().__init__()
        self.sabores = []
        self.precio = 0
        self.sabor_dropdown = ft.Dropdown(
            label="Selecciona un sabor",
            options=[
                ft.dropdown.Option("Vainilla (1 eur)"),
                ft.dropdown.Option("Chocolate (1 eur)"),
                ft.dropdown.Option("Menta (1 eur)"),
                ft.dropdown.Option("Fresa (1 eur)")
            ]
        )
        self.cantidad_sabor = ft.TextField(label="Cantidad", keyboard_type="numero")
        self.mensaje = ft.Text("", color=ft.colors.RED, size=12, visible=False)
        self.list_view = ft.Column()
        self.controls=[
            ft.Text("Heladeria", size=24, weight=ft.FontWeight.BOLD),
            self.sabor_dropdown,
            self.cantidad_sabor,
            self.list_view,
            self.mensaje,
        ]

    def add_to_list(self, e):
        precio = self.precio.value
        cantidad = self.cantidad_sabor.value
        sabor = self.sabor_dropdown
        if cantidad >= 3:
            self.mensaje.value = "Solo puedes elegir un máximo de 3 sabores"
            self.mensaje.color = ft.colors.RED
            self.mensaje.visible  = True
            self.update()
            return
        
        resumen = f" Resumen: \n Sabor: {sabor} \n Cantidad: {cantidad} \n Precio: {precio}"
        self.sabores.append(resumen)
        self.update_resumen_lista()
        self.save_to_file()
        self.cantidad.value = cantidad
        self.update()

    def update_resumen_lista(self):
        self.lista.view.controls.clear()
        for sabores in self.sabores:
            self.lista.view.controls.append(ft.Text(sabores))
        self.update()
        
    def save_to_file(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        with open("data/pedido.txt", "w") as file:
            for sabores in self.sabores:
                file.write(sabores + "\n")

class Recipiente(ft.Column):
    def __init__(self):
        super().__init__()
        self.tarrina = False
        self.cucurucho = False
        self.precio = 0
        self.recipiente_dropdown = ft.Dropdown(
            label="Selecciona un recipiente",
            options=[
                ft.dropdown.Option("Tarrina (1 eur)"),
                ft.dropdown.Option("cucurucho (2 eur)")
            ]
        )


    def add_to_list(self, e):
        precio = self.precio.value
        tarrina = self.tarrina
        cucurucho = self.cucurucho
        eleccion_recipiente = self.recipiente_dropdown
        if eleccion_recipiente == tarrina:
            tarrina == True
        else:
            cucurucho == True    
        resumen = f" Resumen: \n Recipiente: {eleccion_recipiente} \n Precio: {precio}"
        self.pecio.append(resumen)
        self.update_resumen_lista()
        self.save_to_file()
        self.precio.value = precio
        self.update()

        def update_resumen_lista(self):
            self.lista.view.controls.clear()
            self.lista.view.controls.append(ft.Text(eleccion_recipiente))
            self.update()

        def save_to_file(self):
            if not os.path.exists("data"):
                os.makedirs("data")
            with open("data/pedido.txt", "w") as file:
                file.write(eleccion_recipiente + "\n")


class Topping(ft.Column):
    def __init__(self):
        super().__init__()
        self.toppings = []
        self.precio = 0
        self.toppings_dropdown = ft.Dropdown(
            label="Selecciona un extra",
            options=[
                ft.dropdown.Option("Nata (1 eur)"),
                ft.dropdown.Option("Sirope (1 eur)"),
                ft.dropdown.Option("Galletas (1 eur)")
            ]
        )

    def add_to_list(self, e):
        toppings = self.toppings
        precio = self.precio

        resumen = f" Resumen: \n toppings: {toppings} \n Precio: {precio}"
        self.pecio.append(resumen)
        self.update_resumen_lista()
        self.save_to_file()
        self.precio.value = precio
        self.update()

        def update_resumen_lista(self):
            self.lista.view.controls.clear()
            for toppings in self.toppings:
                self.lista.view.controls.append(ft.Text(toppings))
            self.update()

        def save_to_file(self):
            if not os.path.exists("data"):
                os.makedirs("data")
            with open("data/pedido.txt", "w") as file:
                file.write(toppings + "\n")


def main(page: ft.Page):
           
    page.title = "Heladeria"
    page.add(Sabores(), Recipiente(), Topping())
    
ft.app(main)
