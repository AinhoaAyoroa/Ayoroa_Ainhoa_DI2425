from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QToolBar,
    QTextEdit,
    QFileDialog
)
from PySide6.QtGui import QAction
import sys

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de texto plano")
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        toolbar = QToolBar("Menu")
        self.addToolBar(toolbar)

        open_action = QAction("Abrir archivo", self)
        open_action.setToolTip("Abrir un archivo de texto")
        open_action.triggered.connect(self.open_file)
        toolbar.addAction(open_action)

        save_action = QAction("Guardar a archivo", self)
        save_action.setToolTip("Guardar el texto en un archivo")
        save_action.triggered.connect(self.save_file)
        toolbar.addAction(save_action)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_edit.setText(content)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                content = self.text_edit.toPlainText()
                file.write(content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.resize(800, 600) 
    editor.show()
    sys.exit(app.exec())
