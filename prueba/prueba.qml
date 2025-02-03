// main.qml
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Extras 1.15

Rectangle {
    id: root
    width: 400
    height: 300
    color: "#F0F0F0" // Fondo gris claro

    // Fondito con animación sutil
    Gradient {
        id: backgroundGradient
        GradientStop { position: 0.0; color: "#FFFFFF" }
        GradientStop { position: 1.0; color: "#EDEDED" }
    }

    // TRANSICIÓN de color al dar click en el botón
    states: State {
        name: "buttonClicked"
        PropertyChanges {
            target: root
            // color: "#FCEFE8" // si quisieras cambiar de color de fondo al click
        }
    }

    transitions: Transition {
        NumberAnimation {
            properties: "color"
            duration: 800
        }
    }

    // El contenedor principal
    Column {
        id: mainColumn
        anchors.centerIn: parent
        spacing: 16

        // Título
        Text {
            id: title
            text: "Bienvenido"
            font.pointSize: 24
            color: "#333333"
            anchors.horizontalCenter: parent.horizontalCenter
        }

        // Campo de usuario
        TextField {
            id: usernameField
            placeholderText: qsTr("Usuario")
            width: 200
        }

        // Campo de contraseña
        TextField {
            id: passwordField
            placeholderText: qsTr("Contraseña")
            echoMode: TextInput.Password
            width: 200
        }

        // Botón
        Button {
            id: loginButton
            text: qsTr("Iniciar Sesión")
            width: 120
            // Estilo un poco custom
            contentItem: Text {
                text: loginButton.text
                color: "white"
                font.bold: true
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: 8
                color: "#2D89EF"
                border.color: "#1D5FBF"
                border.width: 1
            }

            onClicked: {
                // Activar la transición
                root.state = "buttonClicked"
                
                // Llamar a la función Python expuesta a QML (loginHandler)
                // Solo si ambos campos tienen algo
                if (usernameField.text.length > 0 && passwordField.text.length > 0) {
                    loginHandler.login(usernameField.text, passwordField.text)
                } else {
                    messageLabel.text = "Por favor, completa todos los campos."
                }
            }
        }

        // Label para mostrar feedback (errores, token, etc.)
        Text {
            id: messageLabel
            text: ""
            color: "#d84315" // un tono rojizo para resaltar mensajes de error
            wrapMode: Text.Wrap
            width: 250
            horizontalAlignment: Text.AlignHCenter
        }
    }
}
