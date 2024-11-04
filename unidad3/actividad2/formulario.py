import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        add_button.update()
        page.update()

# TITULOS FORMULARIO
    header = ft.Text("Formulario de registro", theme_style=ft.TextThemeStyle.HEADLINE_LARGE, weight=ft.FontWeight.BOLD)
    title_personal = ft.Text("Datos personales", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM, weight=ft.FontWeight.BOLD)
    title_acceso = ft.Text("Datos de acceso", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM, weight=ft.FontWeight.BOLD)

# CASILLAS 
    fieldNombre = ft.TextField(hint_text="Introduzca el nombre", width=300)
    fieldDirec = ft.TextField(hint_text="Introduzca la dirección", width=300)
    fieldUser = ft.TextField(hint_text="Introduzca el nombre de usuario", width=300)
    fieldContraseña = ft.TextField(password=True, can_reveal_password=True, hint_text="Introduzca la contraseña", width=300)

# DESPLEGABLE
    provincia_drop = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Valencia"),
            ft.dropdown.Option("Madrid"),
            ft.dropdown.Option("Barcelona"),
            ft.dropdown.Option("Málaga"),
            ft.dropdown.Option("Alicante"),
            ft.dropdown.Option("Guipúzcoa"),
            ft.dropdown.Option("Vizcaya"),
            ft.dropdown.Option("La Coruña"),
            ft.dropdown.Option("Otro"),
        ], 
        label="Provincia" 
    )

# ROWS
    # nombre de rows
    nombre = ft.Text("Nombre", weight=ft.FontWeight.BOLD)
    direct = ft.Text("Dirección", weight=ft.FontWeight.BOLD)
    provincia = ft.Text("Provincia", weight=ft.FontWeight.BOLD)
    user = ft.Text("Usuario", weight=ft.FontWeight.BOLD)
    password = ft.Text("Contraseña", weight=ft.FontWeight.BOLD)

    rowNombre = ft.Row([nombre, fieldNombre])
    rowDirect = ft.Row([direct, fieldDirec])
    rowProvin = ft.Row([provincia, provincia_drop])
    rowUser = ft.Row([user, fieldUser])
    rowPass = ft.Row([password, fieldContraseña])


    checkbox = ft.Checkbox(label="Acepto las condiciones de servicio")
    add_button = ft.ElevatedButton("Añadir", disabled=True, on_click=button_clicked)

    page.add(header, title_personal, rowNombre, rowDirect, rowProvin, title_acceso, rowUser, rowPass, checkbox, add_button )

ft.app(target=main)
