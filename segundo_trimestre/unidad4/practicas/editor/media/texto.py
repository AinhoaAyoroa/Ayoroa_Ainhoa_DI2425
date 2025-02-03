from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QToolBar,
    QTextEdit,
    QFileDialog,
)
from PySide6.QtGui import QAction, QKeySequence
import sys

class Editor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de texto")
        self.setFixedSize(800, 800)
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        barra_menus = self.menuBar()
        menu = barra_menus.addMenu("&Menu")

        accion2 = QAction("Abrir archivo", self)
        accion2.setShortcut(QKeySequence("Ctrl+n"))
        accion2.triggered.connect(self.imprimir_por_consola2)

        accion = QAction("&", self)
        accion.setShortcut(QKeySequence("Ctrl+s"))
        accion.triggered.connect(self.imprimir_por_consola)
        menu.addAction(accion)

        self.addToolBar(toolbar)

        abrirArchivo = QAction("Abrir archivo", self)
        abrirArchivo.setToolTip("Abrir un archivo de texto")
        abrirArchivo.triggered.connect(self.guardarArchivo)
        toolbar.addAction(abrirArchivo)

    def abrirArchivo(self):
        ruta_fichero, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")
        if ruta_fichero:
            with open(ruta_fichero, "r", encoding="utf-8") as file:
                contenido = file.read()
                self.textEdit.setText(contenido)

    def guardarArchivo(self):
        ruta_fichero, _ = QFileDialog.getSaveFileName(self, "Guardar archivo, "", Archivos de texto (*.txt)")
        if ruta_fichero:
            with open(ruta_fichero, "w", encoding="utf-8") as file:
                contenido = self.textEdit.toPlainText()
                file.write(contenido)

app = QApplication(sys.argv)
editor = Editor()
editor.show()
sys.exit(app.exec())

