import flet as ft

class LoginApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.width=400
        self.height=300
        self.alignment=ft.MainAxisAlignment.CENTER
        self.horizontal_alignment=ft.CrossAxisAlignment.CENTER
        self.username_field = ft.TextField(label="User", autofocus=True, width=300)
        self.password_field = ft.TextField(
            label="Password", password=True, can_reveal_password=True, width=300
        )
        self.message = ft.Text(size=12, visible=False)
        login_button = ft.ElevatedButton("Submit", on_click=self.login)
        self.controls=[
            ft.Text("Login", size=24, weight=ft.FontWeight.BOLD),
            self.username_field,
            self.password_field,
            self.message,
            login_button,
        ]

    def login(self, e):
        username = self.username_field.value
        password = self.password_field.value

        if username == "admin" and password == "12345":
            self.message.value = "Inicio de sesión exitoso"
            self.message.color = ft.colors.GREEN
            self.message.visible = True
            self.update()
        else:
            self.message.value = "Usuario o contraseña incorrectos"
            self.message.color = ft.colors.RED
            self.message.visible = True
            self.update()

def main(page: ft.Page):
    page.title = "Login"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(LoginApp())

ft.app(target=main)