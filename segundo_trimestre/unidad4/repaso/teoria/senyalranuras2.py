"""Probando Widgets y controles"""

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit  # pylint: disable=no-name-in-module

class FinestraPrincipal(QMainWindow):
    """Clase principal de la ventana."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("finestra")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        vlayout = QVBoxLayout(central_widget)

        self.texto = QLabel("texto")
        self.input = QLineEdit()
        self.input.textChanged.connect(self.settext)

        vlayout.addWidget(self.input)
        vlayout.addWidget(self.texto)

    def settext(self, text: str):
        """Actualiza el contenido del QLabel con el texto del QLineEdit."""
        self.texto.setText(text)

if __name__ == "__main__":
    app = QApplication([])
    ventana = FinestraPrincipal()
    ventana.show()
    app.exec()
