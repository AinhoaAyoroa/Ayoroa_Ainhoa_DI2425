import flet as ft

class ProductApp(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.products = [] 

    def build(self):
        self.name_input = ft.TextField(label="Nom del Producte")
        self.price_input = ft.TextField(label="Preu (€)")
        self.category_input = ft.TextField(label="Categoria")
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

    def add_product(self, e):
        name = self.name_input.value
        price = self.price_input.value
        category = self.category_input.value

        if name and price and category:
            self.products.append((name, price, category))
            self.update_table()
            self.clear_inputs()

    def edit_product(self, e):
        selected_index = self.get_selected_row_index()
        if selected_index is not None:
            name = self.name_input.value
            price = self.price_input.value
            category = self.category_input.value

            if name and price and category:
                self.products[selected_index] = (name, price, category)
                self.update_table()
                self.clear_inputs()

    def delete_product(self, e):
        selected_index = self.get_selected_row_index()
        if selected_index is not None:
            del self.products[selected_index]
            self.update_table()
            self.clear_inputs()

    def update_table(self):
        self.table.rows = []
        for product in self.products:
            name, price, category = product
            self.table.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(name)),
                        ft.DataCell(ft.Text(price)),
                        ft.DataCell(ft.Text(category)),
                    ],
                    on_select_changed=lambda e, idx=len(self.table.rows): self.select_row(idx),
                )
            )
        self.update()

    def clear_inputs(self):
        self.name_input.value = ""
        self.price_input.value = ""
        self.category_input.value = ""
        self.update()

    def get_selected_row_index(self):
        for i, row in enumerate(self.table.rows):
            if row.selected:
                return i
        return None

    def select_row(self, index):
        if 0 <= index < len(self.products):
            name, price, category = self.products[index]
            self.name_input.value = name
            self.price_input.value = price
            self.category_input.value = category
            self.update()


def main(page: ft.Page):
    page.title = "Gestió de Productes"
    page.window_width = 600
    page.window_height = 500
    page.add(ProductApp())


if __name__ == "__main__":
    ft.app(target=main)