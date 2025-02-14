"""Ventana sin layout, ejemplo de como estábamos haciendo una ventana sin layouts"""

from PySide6.QtWidgets import QApplication, QLabel, QWidget  # pylint: disable=no-name-in-module

class Finestra(QWidget):
    """Clase principal"""
    def __init__(self):
        super().__init__()  # Inicializa la clase base
        self.setWindowTitle("finestra")

        self.label1 = QLabel("Etiqueta 1", self)
        self.label2 = QLabel("Etiqueta 2", self)
        self.label2.move(0, 30)

if __name__ == "__main__":
    app = QApplication([])
    finestra = Finestra()
    finestra.show()
    app.exec()
