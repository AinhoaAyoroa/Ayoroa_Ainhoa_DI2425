"""teoría del layout vertical"""

# pylint: disable=no-name-in-module
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton 
)

class VentanaPrincipal(QMainWindow):
    """Clase principal"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle("layout vertical")
        vlayout = QVBoxLayout()

        componente_principal = QWidget()
        componente_principal.setLayout(vlayout)
        self.setCentralWidget(componente_principal)

        vlayout.addWidget(QPushButton("uno"))
        vlayout.addWidget(QPushButton("dos"))
        vlayout.addWidget(QPushButton("tres"))
        vlayout.addWidget(QPushButton("cuatro"))

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()
