"""teoría del layout vertical"""

# pylint: disable=no-name-in-module
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton 
)

class VentanaPrincipal(QMainWindow):
    """Clase principal"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle("layout vertical")
        hlayout = QHBoxLayout()

        componente_principal = QWidget()
        componente_principal.setLayout(hlayout)
        self.setCentralWidget(componente_principal)

        hlayout.addWidget(QPushButton("uno"))
        hlayout.addWidget(QPushButton("dos"))
        hlayout.addWidget(QPushButton("tres"))
        hlayout.addWidget(QPushButton("cuatro"))

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()
