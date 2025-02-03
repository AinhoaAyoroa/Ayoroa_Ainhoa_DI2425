from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 150)

        layout_principal = QVBoxLayout(self)

        # Usuario
        layout_usuario = QHBoxLayout()
        self.label_usuario = QLabel("Usuario:", self)
        self.label_usuario.setFixedSize(100, 30)
        layout_usuario.addWidget(self.label_usuario)

        self.lineEdit_usuario = QLineEdit(self)
        self.lineEdit_usuario.setMaxLength(15)
        self.lineEdit_usuario.setFixedSize(150, 30)
        self.lineEdit_usuario.setPlaceholderText("usuario")
        layout_usuario.addWidget(self.lineEdit_usuario)

        # Contraseña
        layout_contrasena = QHBoxLayout()
        self.label_contrasena = QLabel("Contraseña:", self)
        self.label_contrasena.setFixedSize(100, 30)
        layout_contrasena.addWidget(self.label_contrasena)

        self.lineEdit_contrasena = QLineEdit(self)
        self.lineEdit_contrasena.setMaxLength(20)
        self.lineEdit_contrasena.setFixedSize(150, 30)
        self.lineEdit_contrasena.setPlaceholderText("contraseña")
        self.lineEdit_contrasena.setEchoMode(QLineEdit.Password)
        layout_contrasena.addWidget(self.lineEdit_contrasena)

        # Botón de Login
        layout_botones = QHBoxLayout()
        self.boton_login = QPushButton("Login", self)
        layout_botones.addWidget(self.boton_login, alignment=Qt.AlignCenter)


        layout_principal.addLayout(layout_usuario)
        layout_principal.addLayout(layout_contrasena)
        layout_principal.addLayout(layout_botones)

        # Conexión del botón
        self.boton_login.clicked.connect(self.iniciar_sesion)

    def iniciar_sesion(self):
        usuario = self.lineEdit_usuario.text()
        contrasena = self.lineEdit_contrasena.text()
        
        print(f"Usuario: {usuario}, Contraseña: {contrasena}")

if __name__ == "__main__":
    app = QApplication([])
    ventana = Login()
    ventana.show()
    app.exec()
