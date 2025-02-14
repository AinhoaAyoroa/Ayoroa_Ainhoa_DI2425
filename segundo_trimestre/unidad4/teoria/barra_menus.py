"""Módulo que implementa la ventana principal con menú utilizando PySide6."""

from PySide6.QtWidgets import QApplication, QMainWindow  # pylint: disable=no-name-in-module
from PySide6.QtGui import QAction, QKeySequence  # pylint: disable=no-name-in-module

class VentanaPrincipal(QMainWindow):
    """Clase que define la ventana principal con un menú."""

    def __init__(self):
        """Inicializa la ventana principal y configura el menú."""
        super().__init__()
        self.setMinimumWidth(450)
        self.setWindowTitle("Ventana principal con menú")
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")
        accion = QAction("&Imprimir por consola", self)
        accion.setShortcut(QKeySequence("Ctrl+p"))
        accion.triggered.connect(self.imprimir_por_consola)
        menu.addAction(accion)

    def imprimir_por_consola(self):
        """Imprime un mensaje en consola al activar la acción."""
        print("Acción lanzada a través del menú o del atajo")

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
