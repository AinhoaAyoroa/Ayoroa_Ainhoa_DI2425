"""main del ejercicio"""

import sys
import os

# pylint: disable=no-name-in-module
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidget,
    QAbstractItemView, QHeaderView, QDialog, QVBoxLayout, 
    QFormLayout, QLineEdit, QSpinBox, QDoubleSpinBox,
    QDialogButtonBox, QMenuBar, QMenu, QWidget, QPushButton, QTableWidgetItem
)
from PySide6.QtUiTools import QUiLoader
from database import Database


class ProductDialog(QDialog):
    """Dialógo para añadir y editar productos"""
    def __init__(self, product_data = None):
        super().__init__()
        self.setWindowTitle("Producto")
        self.setup_ui()
        if product_data:
            self.load_product_data(product_data)
    
    def setup_ui(self):
        vlayout = QVBoxLayout()
        form_layout = QFormLayout()

        self.txt_nombre = QLineEdit()
        self.txt_nombre.setPlaceholderText("Nombre del producto")
        form_layout.addRow("Nombre:", self.txt_nom)

        self.txt_precio = QDoubleSpinBox()
        self.txt_precio.setRange(0, 999999.99)
        self.txt_precio.setDecimals(2)
        self.txt_precio.setSuffix(" €")
        form_layout.addRow("Precio:", self.txt_precio)

        self.txt_cantidad = QSpinBox()
        self.txt_cantidad.setRange(0, 999999)
        form_layout.addRow("Cantidad:", self.txt_cantidad)
        vlayout.addLayout(form_layout)

        button_box = QDialogButtonBox()
        button_box.addButton("Aceptar", QDialogButtonBox.AcceptRole)
        button_box.addButton("Cancelar", QDialogButtonBox.RejectRole)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        vlayout.addWidget(button_box)
        self.setLayout(vlayout)
    
    def load_product_data(self, product_data):
        """Cargar datos de los productor existentes en el formulario"""
        self.txt_nombre.setText(str(product_data['nom']))
        self.txt_precio.setValue(float(product_data['precio']))
        self.txt_cantidad.setValueI(int(product_data['cantidad']))

    def get_product_data(self):
        """Obtener la información del formulario"""
        return {
            'nom': self.txt_nombre.text(),
            'precio': self.txt_precio.value(),
            'cantidad': self.txt_cantidad.value()
        }

class ProductApp(QMainWindow):
    """Main de la aplicación"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Productos")
        self.db = Database()
        self.setup_ui()
        self.load_products()

    def setup_ui(self):
        """Configurar la interfaz de usuario de la ventana principal"""
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        vlayout = QVBoxLayout(widget_central)

        menubar = QMenuBar()
        self.setMenuBar(menubar)

        menu_productos = QMenu("&Productos", self)
        menubar.addMenu(menu_productos)

        menu_productos.addAction("&Añadir", self.show_add_dialog)
        menu_productos.addAction("&Modificar", self.show_modify_dialog)

        self.tabla_widget = QTableWidget()
        self.tabla_widget.setColumnCount(4)
        self.tabla_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Precio", "Cantidad"])
        self.tabla_widget.setColumnHidden(0, True)
        self.tabla_widget.setSelectionBehavior(1)
        self.tabla_widget.setEditTriggers(0)

    def load_products(self):
        """Carrega els productes a la taula."""
        self.ui.tableWidget.setRowCount(0)
        products = self.db.get_all_products()

        for row_index, product in enumerate(products):
            self.ui.tableWidget.insertRow(row_index)
            for col_index, data in enumerate(product):
                self.ui.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(data)))

    def add_product(self):
        """Afegeix un nou producte."""
        nom = self.ui.txtNom.text()
        preu = self.ui.txtPreu.text()
        quantitat = self.ui.txtQuantitat.text()

        if nom and preu and quantitat:
            self.db.add_product(nom, float(preu), int(quantitat))
            self.load_products()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Error", "Tots els camps són obligatoris")

    def update_product(self):
        """Modifica el producte seleccionat."""
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un producte per modificar")
            return

        product_id = int(self.ui.tableWidget.item(selected_row, 0).text())
        nom = self.ui.txtNom.text()
        preu = self.ui.txtPreu.text()
        quantitat = self.ui.txtQuantitat.text()

        if nom and preu and quantitat:
            self.db.update_product(product_id, nom, float(preu), int(quantitat))
            self.load_products()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Error", "Tots els camps són obligatoris")

    def delete_product(self):
        """Elimina el producte seleccionat."""
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un producte per eliminar")
            return

        product_id = int(self.ui.tableWidget.item(selected_row, 0).text())
        self.db.delete_product(product_id)
        self.load_products()
        self.clear_inputs()

    def load_selected_product(self):
        """Carrega les dades del producte seleccionat als camps d’entrada."""
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:
            self.ui.txtNom.setText(self.ui.tableWidget.item(selected_row, 1).text())
            self.ui.txtPreu.setText(self.ui.tableWidget.item(selected_row, 2).text())
            self.ui.txtQuantitat.setText(self.ui.tableWidget.item(selected_row, 3).text())

    def clear_inputs(self):
        """Buida els camps d’entrada."""
        self.ui.txtNom.clear()
        self.ui.txtPreu.clear()
        self.ui.txtQuantitat.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductApp()
    sys.exit(app.exec())
