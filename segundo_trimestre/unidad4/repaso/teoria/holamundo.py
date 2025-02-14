"""Hola mundo de PySide6"""

from PySide6.QtWidgets import QApplication, QLabel, QWidget  # pylint: disable=no-name-in-module

class Finestra(QWidget):
    """Clase Finestra hereda de QWidget, componente base."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("finestra")
        self.etiqueta1 = QLabel("Hola mundo!", self)

if __name__ == "__main__":
    app = QApplication([])
    finestra1 = Finestra()
    finestra1.show()
    app.exec()
