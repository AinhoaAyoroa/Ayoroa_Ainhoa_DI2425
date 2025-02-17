import flet as ft

def main(page: ft.Page):
    page.title = "Loguin"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def password_correcta(e):
        secret_pass = 1234
        try:
            if int(password.value) == secret_pass:
                page.clean()
                page.add(ft.Text("Logeado como admin",
                                size=30))
            else:
                open_dlg_modal()
        except ValueError:
            open_dlg_modal()

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    def open_dlg_modal():
        dlg_modal.open = True
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("No es posible iniciar sesión"),
        content=ft.Text("Usuario o contraseña incorrectos!"),
        actions=[
            ft.TextButton("Ok", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    nom = ft.TextField(label="Usuario")
    password = ft.TextField(label="Contraseña", password=True)

    page.add(
        ft.Column(
            [
                nom,
                password,
                ft.ElevatedButton("Submit", on_click=password_correcta),
            ],
            width=300,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    page.dialog = dlg_modal  

ft.app(target=main)