import sqlite3
from contextlib import contextmanager
from typing import Optional , Dict , List

@contextmanager
def get_connection():
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
def create_table():
    with get_connection() as conn:
      conn.execute("""CREATE TABLE IF NOT EXIST(id INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT UNIQUE NOT NULL,price REAL NOT NULL , stock INTEGER NOT NULL DEFAULT 0, created_at TEXT DEFAULT CURRENT_TIMESTAMP)""")
      conn.commit()
      print("tabla creada con exito")
def add_prodduct(name:str,price:float,stock:int) -> bool:
    try:
        with get_connection() as conn:
            conn.execute("INSERT INTO products(name,price,stock)VALUES(?,?,?)" , (name,price,stock))
            conn.commit()
            print(f"producto {name} agregado")
            return True
    except sqlite3.IntegrityError:
        print(f" Error el producto {name} ya existe")
        return False
    except Exception as e:
        print(f" error inesperado {e}")
        return False
def get_all_products() -> List[Dict]:
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM products ORDER BY NAME")
        return [dict(row) for row in cursor.fetchall()]
def get_product_by_name(name:str) -> Optional[dict]:
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM products Where name = ?",(name,))
        row = cursor.fetchone()
        return dict(row) if row else None
    




