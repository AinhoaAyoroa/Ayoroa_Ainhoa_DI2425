# ACTIVIDAD - REALIZA UN PROGRAMA QUE SE VEA ASÍ:
# layout
# layout layout layout layout layout
# layout
# layout

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout cuadrícula")

        layout_cuadrícula = QGridLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_cuadrícula)
        self.setCentralWidget(componente_principal)

        layout_cuadrícula.addWidget(QPushButton('V1'), 0, 0)
        layout_cuadrícula.addWidget(QPushButton('V2'), 1, 0)
        layout_cuadrícula.addWidget(QPushButton('V3'), 2, 0)
        layout_cuadrícula.addWidget(QPushButton('V4'), 3, 0)

        layout_cuadrícula.addWidget(QPushButton('H1'), 1, 1)
        layout_cuadrícula.addWidget(QPushButton('H2'), 1, 2)
        layout_cuadrícula.addWidget(QPushButton('H3'), 1, 3)
        layout_cuadrícula.addWidget(QPushButton('H4'), 1, 4)
    


app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()