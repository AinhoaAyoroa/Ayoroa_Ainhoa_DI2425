import flet as ft

def main(page: ft.Page):
    page.title = "Llista de la Compra"
    
    archivo_datos = "data/llista_compra.txt"
    
    import pathlib
    data_folder = pathlib.Path("data")
    data_folder.mkdir(exist_ok=True)
    
    def guardar_llista():
        with open(archivo_datos, "w", encoding="utf-8") as f:
            for item in llista_items.controls:
                f.write(f"{item.data['categoria']} - {item.data['descripcio']} - {item.data['quantitat']}\n")
    
    def afegir_a_llista(e):
        if not input_descripcio.value or not input_quantitat.value.isdigit():
            ft.AlertDialog(title="Error", content=ft.Text("Introdueix una descripció i una quantitat vàlida.")).show()
            return
        item = ft.ListTile(
            title=ft.Text(input_descripcio.value),
            subtitle=ft.Text(f"Categoria: {dropdown_categoria.value}, Quantitat: {input_quantitat.value}"),
            trailing=ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: eliminar_item(item)),
            data={
                "categoria": dropdown_categoria.value,
                "descripcio": input_descripcio.value,
                "quantitat": input_quantitat.value,
            },
        )
        llista_items.controls.append(item)
        input_descripcio.value = ""
        input_quantitat.value = ""
        llista_items.update()
        guardar_llista()

    def eliminar_item(item):
        llista_items.controls.remove(item)
        llista_items.update()
        guardar_llista()

    dropdown_categoria = ft.Dropdown(
        options=[
            ft.dropdown.Option("Aliments"),
            ft.dropdown.Option("Productes d'higiene"),
            ft.dropdown.Option("Material d'oficina"),
            ft.dropdown.Option("Altres"),
        ],
        value="Aliments",
        label="Categoria",
    )
    
    input_descripcio = ft.TextField(label="Descripció del producte")
    input_quantitat = ft.TextField(label="Quantitat", keyboard_type=ft.KeyboardType.NUMBER)
    boto_afegir = ft.ElevatedButton("Afegir a la llista", on_click=afegir_a_llista)
    
    llista_items = ft.ListView(expand=True)

    try:
        with open(archivo_datos, "r", encoding="utf-8") as f:
            for linia in f:
                categoria, descripcio, quantitat = linia.strip().split(" - ")
                item = ft.ListTile(
                    title=ft.Text(descripcio),
                    subtitle=ft.Text(f"Categoria: {categoria}, Quantitat: {quantitat}"),
                    trailing=ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: eliminar_item(item)),
                    data={
                        "categoria": categoria,
                        "descripcio": descripcio,
                        "quantitat": quantitat,
                    },
                )
                llista_items.controls.append(item)
    except FileNotFoundError:
        pass

    page.add(
        ft.Column(
            [
                dropdown_categoria,
                input_descripcio,
                input_quantitat,
                boto_afegir,
                ft.Text("Llista de la compra:"),
                llista_items,
            ],
            scroll="adaptive",
        )
    )

ft.app(target=main)