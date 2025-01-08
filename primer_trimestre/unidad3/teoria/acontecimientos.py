import flet as ft
# añadir el enter y ademas controlar que el enter no añada espacios

def main(page):
    def add_clicked(e):
        if add_button.disabled!=True:
            page.add(ft.Checkbox(label=new_task.value.strip()))
        new_task.value = ""
        add_button.disabled = True
        add_button.update() 
        new_task.focus()
        new_task.update()

    def text_changed(e):
        add_button.disabled=new_task.value.strip()==""
        add_button.update()

    new_task = ft.TextField(hint_text="Tasca pendent", width=300, on_change=text_changed, on_submit=add_clicked)
    add_button = ft.ElevatedButton("Afegir", disabled=True, on_click=add_clicked)
    page.add(ft.Row([new_task, add_button]))

ft.app(target=main)