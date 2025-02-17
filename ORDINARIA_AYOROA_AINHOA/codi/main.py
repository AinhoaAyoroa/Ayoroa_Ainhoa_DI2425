from PySide6.QtWidgets import QDialog, QDialogButtonBox, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QPushButton, QHeaderView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QAction

from database import Database
import sys
import os

class DialogoPersonalizado(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Dialogo")

        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.caja_botones = QDialogButtonBox(botones)
        self.caja_botones.accepted.connect(self.accept)
        self.caja_botones.rejected.connect(self.reject)

        self.layout_dialogo = QVBoxLayout()
        self.layout_dialogo.addWidget(
            QLabel("¿Estás seguro de querer realizar esta acción?"))
        self.layout_dialogo.addWidget(self.caja_botones)
        self.setLayout(self.layout_dialogo)


class ProductApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestió de Productes")
        self.setGeometry(100, 100, 600, 500)
        self.db = Database()

        # Widget principal
        loader = QUiLoader()
        interface_path = os.path.join(os.path.dirname(__file__), "products.ui")
        self.ui = loader.load(interface_path, None)
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.layout = QVBoxLayout()
        main_widget.setLayout(self.layout)
        barra_menus = self.menuBar()

        menu = barra_menus.addMenu("&Productes")
        accion = QAction("&Afegir producte", self)
        accion.triggered.connect(self.add_product)
        menu.addAction(accion)
        accion2 = QAction("&Modificar producte", self)
        accion2.triggered.connect(self.edit_product)
        menu.addAction(accion2)

        self.delete_button = QPushButton("Eliminar producte")
        self.delete_button.clicked.connect(self.mostrar_dialogo_delete)
        self.layout.addWidget(self.delete_button)
        

        self.table = self.create_table()
        self.layout.addWidget(self.table)

        self.load_products()
        
    def mostrar_dialogo_delete(self):
        ventana_dialogo = DialogoPersonalizado(self)
        ventana_dialogo.setWindowTitle("Confirmar Eliminación")
        resultado = ventana_dialogo.exec()
        if resultado:
            self.delete_product(self.table.currentRow())    

    def create_table(self):
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Nom", "Preu", "Categoria"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setSelectionBehavior(QTableWidget.SelectRows)
        return table

    def load_products(self):
        self.table.setRowCount(0)
        products = self.db.get_products()
        for row_index, (product_id, name, price, category) in enumerate(products):
            self.table.insertRow(row_index)
            self.table.setItem(row_index, 0, QTableWidgetItem(name))
            self.table.setItem(row_index, 1, QTableWidgetItem(f"{float(price):.2f}"))
            self.table.setItem(row_index, 2, QTableWidgetItem(category))

    def add_product(self):
        self.ui.addname.clear()
        self.ui.addprice.clear()
        self.ui.addcat.setCurrentIndex(0)
        res = self.ui.exec()

        if res:
            ventana_dialogo = DialogoPersonalizado(self)
            ventana_dialogo.setWindowTitle("Confirmar alta producte")
            resultado = ventana_dialogo.exec()
            if resultado:
                name = self.ui.addname.text()
                price = self.ui.addprice.text()
                category = self.ui.addcat.currentText()
                if name and price and category:
                    self.db.add_product(name, float(price), category)  
                    self.load_products()
                

    def edit_product(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            return
        
        product_data = self.db.get_products()[selected_row]
        self.ui.addname.setText(product_data[1])  
        self.ui.addprice.setValue(float(product_data[2]))  
        self.ui.addcat.setCurrentText(product_data[3]) 

        res = self.ui.exec()
        if res:
            ventana_dialogo = DialogoPersonalizado(self)
            ventana_dialogo.setWindowTitle("Confirmar modificación")
            resultado = ventana_dialogo.exec()
            if resultado:
                user_id = product_data[0]
                new_name = self.ui.addname.text()
                new_price = self.ui.addprice.text()
                new_cat = self.ui.addcat.currentText()

                if new_name and new_price and new_cat:
                    self.db.update_product(user_id, new_name, float(new_price), new_cat)  
                    self.load_products()

    def delete_product(self, row):
        if row == -1:
            return
        product_id = self.db.get_products()[row][0]
        self.db.delete_product(product_id)
        self.load_products()

if __name__ == "__main__":
    from PySide6.QtCore import Qt
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)  # evitar error raro de la interfaz
    app = QApplication(sys.argv)
    window = ProductApp()
    window.show()
    sys.exit(app.exec())