import os
import sqlite3
import pytest
from main import ProductApp
from PySide6.QtWidgets import QApplication

def test_afegir(qtbot):
    """Inicializa la aplicación, realiza la prueba y limpia la base de datos."""
    test_db = "test_products.db"
    if os.path.exists(test_db):
        os.remove(test_db)
    
    conn = sqlite3.connect(test_db)
    conn.execute('''CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        price TEXT NOT NULL,
        category TEXT NOT NULL
    )''')
    conn.close()
    
    app = ProductApp() 
    app.db.conn = sqlite3.connect(test_db) 
    app.db.cursor = app.db.conn.cursor()
    qtbot.addWidget(app)
    
    app.db.add_product("productoPrueba", "15", "Limpieza")
    app.load_products()
    assert app.table.rowCount() == 1
    
    app.close()
    os.remove(test_db)
