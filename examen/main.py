import flet as ft

def main(page: ft.Page):
    page.title = "Test Pyside6 Venv"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    label = ft.Text("Flet está funcionando correctamente", size=20, weight=ft.FontWeight.BOLD)
    page.add(label)

if __name__ == "__main__":
    ft.app(target=main)
