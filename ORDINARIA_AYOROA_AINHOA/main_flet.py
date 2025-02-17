import flet as ft

class ProductApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.products = []  
        self.selected_index = None  

    def build(self):
        self.name_input = ft.TextField(label="Nom del Producte")
        self.price_input = ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=self.decrement_price),
                ft.TextField(label="Preu (€)", value="0", width=100, text_align=ft.TextAlign.RIGHT),
                ft.IconButton(ft.icons.ADD, on_click=self.increment_price),
            ],
            alignment=ft.MainAxisAlignment.START,
        )
        self.category_input = ft.Dropdown(
            label="Categoria",
            options=[
                ft.dropdown.Option("limpieza"),
                ft.dropdown.Option("electronica"),
                ft.dropdown.Option("bricolaje"),
            ],
        )
        self.add_button = ft.ElevatedButton("Afegir Producte", on_click=self.add_product)
        self.edit_button = ft.ElevatedButton("Modificar Producte", on_click=self.edit_product)
        self.delete_button = ft.ElevatedButton("Eliminar Producte", on_click=self.delete_product)
        self.table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nom")),
                ft.DataColumn(ft.Text("Preu")),
                ft.DataColumn(ft.Text("Categoria")),
            ],
            rows=[],
        )
        return ft.Column(
            controls=[
                self.name_input,
                self.price_input,
                self.category_input,
                ft.Row(controls=[self.add_button, self.edit_button, self.delete_button]),
                self.table,
            ]
        )

    def increment_price(self, e):
        current_price = int(self.price_input.controls[1].value)
        self.price_input.controls[1].value = float(current_price + 1)
        self.update()

    def decrement_price(self, e):
        current_price = int(self.price_input.controls[1].value)
        if current_price > 0:
            self.price_input.controls[1].value = float(current_price - 1)
            self.update()

    def add_product(self, e):
        name = self.name_input.value
        price = self.price_input.controls[1].value
        category = self.category_input.value

        if name and price and category:
            self.products.append((name, price, category))
            self.update_table()
            self.clear_inputs()

    def edit_product(self, e):
        if self.selected_index is not None:
            name = self.name_input.value
            price = self.price_input.controls[1].value
            category = self.category_input.value

            if name and price and category:
                self.products[self.selected_index] = (name, price, category)
                self.update_table()
                self.clear_inputs()
                self.selected_index = None

    def delete_product(self, e):
        if self.selected_index is not None:
            del self.products[self.selected_index]
            self.update_table()
            self.clear_inputs()
            self.selected_index = None

    def update_table(self):
        self.table.rows = []
        for idx, product in enumerate(self.products):
            name, price, category = product
            self.table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(name)),
                        ft.DataCell(ft.Text(price)),
                        ft.DataCell(ft.Text(category)),
                    ],
                    on_select_changed=lambda e, index=idx: self.select_row(index),
                )
            )
        self.update()

    def clear_inputs(self):
        self.name_input.value = ""
        self.price_input.controls[1].value = "0"
        self.category_input.value = ""
        self.update()

    def select_row(self, index):
        if 0 <= index < len(self.products):
            self.selected_index = index
            name, price, category = self.products[index]
            self.name_input.value = name
            self.price_input.controls[1].value = price
            self.category_input.value = category
            self.update()

def main(page: ft.Page):
    page.title = "Gestió de Productes"
    page.window_width = 600
    page.window_height = 500
    page.add(ProductApp())

if __name__ == "__main__":
    ft.app(target=main)
