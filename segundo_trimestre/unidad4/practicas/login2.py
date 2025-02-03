from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 300)
        layout_vertical_principal = QVBoxLayout(self)
    
        # U S U A R I O
        layout_horizontal_user = QHBoxLayout()
        self.label_usuario = QLabel("Usuario:", self)
        self.label_usuario.setFixedSize(100, 30)
        layout_horizontal_user.addWidget(self.label_usuario)

        self.lineEdit_usuario = QLineEdit(self)
        self.lineEdit_usuario.setMaxLength(15)
        self.lineEdit_usuario.setFixedSize(150, 30)
        self.lineEdit_usuario.setPlaceholderText("usuario")
        layout_horizontal_user.addWidget(self.lineEdit_usuario)

        # C O N T R A S E Ñ A
        layout_horizontal_passwd = QHBoxLayout()
        self.label_contrasena = QLabel("Contraseña:", self)
        self.label_contrasena.setFixedSize(100, 30)
        layout_horizontal_passwd.addWidget(self.label_contrasena)

        self.lineEdit_contrasena = QLineEdit(self)
        self.lineEdit_contrasena.setMaxLength(20)  
        self.lineEdit_contrasena.setFixedSize(150, 30) 
        self.lineEdit_contrasena.setPlaceholderText("contraseña")
        self.lineEdit_contrasena.setEchoMode(QLineEdit.Password)
        layout_horizontal_passwd.addWidget(self.lineEdit_contrasena)
        
        # B O T Ó N
        layout_botones = QHBoxLayout()
        self.boton_login = QPushButton("Login", self)
        layout_botones.addWidget(self.boton_login, alignment=Qt.AlignCenter)

        layout_vertical_principal.addLayout(layout_horizontal_user)
        layout_vertical_principal.addLayout(layout_horizontal_passwd)
        layout_vertical_principal.addLayout(layout_botones)

       # self.boton.clicked.connect(self.iniciar_sesion)



app = QApplication([])
ventana = Login()
ventana.show()
app.exec()
