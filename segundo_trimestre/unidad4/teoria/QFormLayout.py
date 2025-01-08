# TODO - CAMBIAR ORIENTACIÓN DEL SLIDER

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFormLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QSlider
)
from PySide6.QtCore import Qt

class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout formulario")
        self.setMinimumWidth(360)

        layout_formulario = QFormLayout()
        componente_principal = QWidget()
        componente_principal.setLayout(layout_formulario)
        self.setCentralWidget(componente_principal)

        layout_formulario.addRow(QLabel("Texto: "), QLineEdit())
        layout_formulario.addRow(QLabel("Entero: "), QSpinBox())

        self.dial1 = QSlider()
        self.dial1 = QSlider(orientation=Qt.o)

        layout_formulario.addRow(QLabel("Decimal: "), ())

app = QApplication([])

ventana = VentanaPrincipal()
ventana.show()

app.exec()