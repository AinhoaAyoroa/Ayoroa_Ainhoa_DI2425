from PySide6.QtWidgets import QApplication, QLabel, QWidget

class Finestra(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("finestra")

        # Creem dues etiquetes amb el component com a parent
        self.label1 = QLabel("Etiqueta 1", self)
        self.label2 = QLabel("Etiqueta 2", self)
        # Necessitem moure la segona perquè no es solapi amb la primera
        self.label2.move(0, 30)

if __name__ == "__main__":
    app = QApplication([])
    finestra = Finestra()
    # Mostrem la finestra
    finestra.show()
    app.exec()