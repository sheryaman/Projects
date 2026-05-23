import sqlite3
import tkinter as tk
from tkinter import ttk



def create_table():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT , price REAL , stock INTEGER)""")
    conn.commit()
    conn.close()
def add_product(name,price,stock):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products(name,price,stock) VALUES (?,?,?)",(name,price,stock))
    conn.commit()
    conn.close()
def get_all_products():
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return [dict(product) for product in products]
def Search_by_name(name):
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.execute("SELECT * From products WHERE LOWER(name) = LOWER(?)", (name,))
    product = cursor.fetchone()
    conn.close()
    return dict(product) if product else None

def update_stock(name,new_stock):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET stock = ? WHERE name = ?",(new_stock,name))
    conn.commit()
    conn.close()
def delete_product(name):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE name = ?", (name,))
    conn.commit()
    conn.close()
create_table()
conn = sqlite3.connect("store.db")
conn.execute("DELETE FROM products")
conn.commit()
conn.close()
add_product("Laptop", 2500, 10)
add_product("Mouse", 80, 50)
add_product("Teclado", 150, 30)
update_stock("Mouse", 45)
delete_product("Teclado")
for product in get_all_products():
    print(f"{product['name']} - S/ {product['price']} - Stock: {product['stock']}")

while True:
 option = input("Storage Manager \n1.-Show all \n2.-Search product \n3.-Add product \n4.-Update Product \n5.-Delete Product \n6.-Exit \n")
 if option == "1":
    for p in get_all_products():
       print(f"{p['name']} - S/ {p['price']} - Stock: {p['stock']}")
 elif option == "2":
     while True:
      name = input("Product Name \n")
      result = Search_by_name(name)
      if result:
       print(f"{result['name']} - S/ {result['price']} - Stock: {result['stock']}")
       break
      else:
        print("Product not Found , Try Again")
 elif option == "3":
    name = input("Name product")
    price = float(input("price product"))
    stock = int(input("how many stock is there ?"))
    result = add_product(name,price,stock)
    print("product add succesfully " if result else "Incorrect Sintaxis" )
 elif option == "4":
    name = input("Product name")
    new_stock = int(input("How many stock is there?"))
    result = update_stock(name,new_stock)
    print("Upgraded sucessfully" if result else "Incorrect Sintaxis")
 elif option == "5":
    name = input("What product are you going to delete?")
    result = delete_product(name)
    print("Product Deleted Sucessfully" if result else "incorrect product")
 elif option == "6":
    break
               
