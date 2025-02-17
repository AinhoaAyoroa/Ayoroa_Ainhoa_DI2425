#!/usr/bin/env python3
"""
Módulo de base de datos.

Este módulo provee la clase Database para gestionar una base de datos SQLite destinada
a almacenar productos. La clase Database se encarga de crear la tabla de productos y de
realizar operaciones CRUD: obtener, añadir, actualizar y eliminar productos.
"""

import sqlite3


class Database:
    """Clase para gestionar la base de datos SQLite de productos."""

    def __init__(self, db_name="database.db"):
        """
        Inicializa la instancia de la base de datos.

        Se conecta a la base de datos SQLite con el nombre proporcionado (por defecto "database.db")
        y crea la tabla de productos si no existe.

        Args:
            db_name (str): El nombre del archivo de la base de datos SQLite.
        """
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """
        Crea la tabla de productos si no existe.

        La tabla 'productes' tiene las siguientes columnas:
            - id: INTEGER, clave primaria, autoincrementable.
            - nom: TEXT, no nulo.
            - preu: REAL, no nulo.
            - quantitat: INTEGER, no nulo.
        """
        query = """
        CREATE TABLE IF NOT EXISTS productes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            preu REAL NOT NULL,
            quantitat INTEGER NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def get_all_products(self):
        """
        Obtiene todos los productos de la base de datos.

        Returns:
            list: Una lista de tuplas, donde cada tupla representa un registro de producto.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM productes")
        return cursor.fetchall()

    def add_product(self, nom, preu, quantitat):
        """
        Añade un nuevo producto a la base de datos.

        Args:
            nom (str): El nombre del producto.
            preu (float): El precio del producto.
            quantitat (int): La cantidad del producto.
        """
        query = "INSERT INTO productes (nom, preu, quantitat) VALUES (?, ?, ?)"
        self.conn.execute(query, (nom, preu, quantitat))
        self.conn.commit()

    def update_product(self, product_id, nom, preu, quantitat):
        """
        Actualiza un producto existente en la base de datos.

        Args:
            product_id (int): El ID del producto a actualizar.
            nom (str): El nuevo nombre del producto.
            preu (float): El nuevo precio del producto.
            quantitat (int): La nueva cantidad del producto.
        """
        query = "UPDATE productes SET nom=?, preu=?, quantitat=? WHERE id=?"
        self.conn.execute(query, (nom, preu, quantitat, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        """
        Elimina un producto de la base de datos.

        Args:
            product_id (int): El ID del producto a eliminar.
        """
        query = "DELETE FROM productes WHERE id=?"
        self.conn.execute(query, (product_id,))
        self.conn.commit()
