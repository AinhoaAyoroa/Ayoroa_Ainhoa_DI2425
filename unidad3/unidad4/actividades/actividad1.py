from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QLabel
)

class actividad1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actividad - 1")
        self.setFixedSize(350, 100)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setMaxLength(5)  
        self.lineEdit.setFixedSize(50, 30) 
        self.lineEdit.move(20, 20)

        self.label = QLabel("...", self)
        self.label.setFixedSize(50, 30)  
        self.label.move(80, 20)

        self.lineEdit.textChanged.connect(self.update_label)

    def update_label(self, text):
        self.label.setText(text)

app = QApplication([]) 
window = actividad1() 
window.show()  
app.exec()  

