# main.py
import sys
import json
import requests

# pylint: disable=no-name-in-module
from PySide6.QtCore import QUrl, QObject, Signal, Slot, Property
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

class LoginHandler(QObject):
    """
    Clase que maneja la lógica de login.
    Será expuesta a QML para que la UI llame a login().
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        self._jwt_token = None

    # --- SIGNALS ---
    messageChanged = Signal(str)      # Para notificar a QML cuando cambie el mensaje
    tokenReceived = Signal(str)       # Para notificar a QML cuando llegue un token (opcional)

    # --- PROPERTIES ---
    @Property(str, notify=messageChanged)
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        if value != self._message:
            self._message = value
            self.messageChanged.emit(value)

    # --- SLOTS ---
    @Slot(str, str)
    def login(self, username, password):
        """
        Petición POST al servidor Node para autenticación.
        Al terminar, se actualizará self.message que impactará en QML.
        """
        login_url = "http://tu-servidor-node.com/auth/login"  # Ajustar la URL
        headers = {"Content-Type": "application/json"}
        payload = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(login_url, headers=headers, json=payload, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if "token" in data:
                    self._jwt_token = data["token"]
                    self.message = "¡Login exitoso! Token: " + self._jwt_token[:10] + "..."
                    self.tokenReceived.emit(self._jwt_token)
                else:
                    error_message = data.get("error", "Error no especificado")
                    self.message = f"No se recibió token: {error_message}"
            else:
                self.message = f"Error del servidor: {response.status_code}"
        except requests.RequestException as e:
            self.message = f"Fallo de conexión: {e}"

def main():
    app = QApplication(sys.argv)

    # Instanciamos nuestro 'controlador de login'
    login_handler = LoginHandler()

    # Cargamos QML
    engine = QQmlApplicationEngine()
    # Exponer 'loginHandler' a QML bajo el nombre "loginHandler"
    engine.rootContext().setContextProperty("loginHandler", login_handler)

    # Cargar el archivo QML
    engine.load(QUrl.fromLocalFile("main.qml"))

    # Verificar si hubo problemas al cargar QML
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
