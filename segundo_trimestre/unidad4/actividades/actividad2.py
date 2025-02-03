# ACTIVIDAD - REALIZA UN PROGRAMA QUE SE VEA ASÍ:
# layout
# layout layout layout layout layout
# layout
# layout

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QWidget, 
    QVBoxLayout, 
    QPushButton,
    QHBoxLayout
)


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout cuadrícula")

        layout_vertical = QVBoxLayout()
        layout_horizontal = QHBoxLayout()
        
        componente_secundario = QWidget()
        componente_secundario.setLayout(layout_horizontal)
        self.setCentralWidget(componente_secundario)

        layout_vertical.addWidget(QPushButton('V1'))
        layout_vertical.addWidget(QPushButton('V2'))
        layout_vertical.addWidget(QPushButton('V3'))
        layout_vertical.addWidget(QPushButton('V4'))

        componente_secundario = QWidget()
        componente_secundario.setLayout(layout_vertical)

        layout_horizontal.addWidget(componente_secundario)
        layout_horizontal.addWidget(QPushButton('H1'))
        layout_horizontal.addWidget(QPushButton('H2'))
        layout_horizontal.addWidget(QPushButton('H3'))
        layout_horizontal.addWidget(QPushButton('H4'))
    


app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()
app.exec()