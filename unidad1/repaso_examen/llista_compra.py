import flet as ft
import os

class ShoppingListApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.products = []
        self.category_dropdown = ft.Dropdown(
            label="Selecciona una categoria",
            options=[
                ft.dropdown.Option("Aliments"),
                ft.dropdown.Option("Productes d'higiene"),
                ft.dropdown.Option("Material d'oficina"),
                ft.dropdown.Option("Altres")
            ]
        )
        
        self.product_description = ft.TextField(label="Descripció del producte")
        self.product_quantity = ft.TextField(label="Quantitat", keyboard_type="number")
        
        self.message = ft.Text("", color=ft.colors.RED, size=12, visible=False)
        
        add_button = ft.ElevatedButton("Afegir a la llista", on_click=self.add_to_list)
        remove_button = ft.ElevatedButton("Eliminar de la llista", on_click=self.remove_from_list)
        
        self.list_view = ft.Column()
        
        self.controls=[
            ft.Text("Aplicació de Llista de la Compra", size=24, weight=ft.FontWeight.BOLD),
            self.category_dropdown,
            self.product_description,
            self.product_quantity,
            add_button,
            remove_button,
            self.list_view,
            self.message,
        ]

    def add_to_list(self, e):
        category = self.category_dropdown.value
        description = self.product_description.value.strip()
        quantity = self.product_quantity.value

        if not description:
            self.message.value = "La descripció del producte no pot estar buida!"
            self.message.color = ft.colors.RED
            self.message.visible = True
            self.update()
            return

        product = f"{description} - {category} - Quantitat: {quantity}"
        self.products.append(product)
        self.update_product_list()
        
        self.save_to_file()
        
        self.product_description.value = ""
        self.product_quantity.value = 1
        self.update()
        
    def remove_from_list(self, e):
        category = self.category_dropdown.value
        description = self.product_description.value.strip()

        if not description:
            self.message.value = "Introdueix una descripció per eliminar un producte."
            self.message.color = ft.colors.RED
            self.message.visible = True
            self.update()
            return

        product_to_remove = f"{description} - {category}"
        if product_to_remove in self.products:
            self.products.remove(product_to_remove)
            self.update_product_list()
            self.save_to_file()
            self.message.value = f"Producte '{description}' eliminat."
            self.message.color = ft.colors.GREEN
            self.message.visible = True
        else:
            self.message.value = "Producte no trobat a la llista."
            self.message.color = ft.colors.RED
            self.message.visible = True
        self.update()
    
    def update_product_list(self):
        self.list_view.controls.clear()
        for product in self.products:
            self.list_view.controls.append(ft.Text(product))
        self.update()

    def save_to_file(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        
        with open("data/shopping_list.txt", "w") as file:
            for product in self.products:
                file.write(product + "\n")


def main(page: ft.Page):
    page.title = "Aplicació de Llista de la Compra"
    page.add(ShoppingListApp())

ft.app(main)
