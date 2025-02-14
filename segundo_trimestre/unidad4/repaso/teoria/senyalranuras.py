"""Fichero de teoría de las señales y ranuras"""

from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow # pylint: disable=no-name-in-module

class FinestraPrincipal(QMainWindow):
    """CLase FinestraPrincipal, hereda de QMainWindow. El QMainWindow es un componente
    pensado para ser la ventana principal de una apliación"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("finestra")
        self.boton1 = QPushButton("Haz clic!")
        self.setCentralWidget(self.boton1)
        self.boton1.clicked.connect(self.clic_de_boton)

    def clic_de_boton(self):
        """funcioón para hacer funcionar el clic en el botón"""
        print("señal de clic botón recibido -> ejecución de la ranura")

if __name__ == "__main__":
    app = QApplication([])
    finestra1 = FinestraPrincipal()
    finestra1.show()
    app.exec()
