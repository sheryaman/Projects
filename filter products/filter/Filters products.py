import sqlite3
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
def create_table():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL UNIQUE)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT NOT NULL UNIQUE , price REAL NOT NULL ,stock INTEGER NOT NULL ,category_id INTEGER, FOREIGN KEY(category_id) REFERENCES categories(id))""")
    conn.commit()
    conn.close()
def add_category(name):
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
def get_all_categories():
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    conn.close()
    return [dict(c) for c in categories]
def get_category_id(name):
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM categories WHERE LOWER(name) = LOWER(?)",(name,))
    category_id = cursor.fetchone()
    conn.close()
    return category_id["id"] if category_id else None
def add_products(name,price,stock,category_name):
    category_id = get_category_id(category_name)
    if not category_id:
        messagebox.showinfo("Warning", f"Category '{category_name}' doesn't exist")
        return
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO products(name,price,stock,category_id) VALUES(?,?,?,?)",(name,price,stock,category_id))
    conn.commit()
    conn.close()
def  get_all_products():
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(""" SELECT products.id, products.name ,products.price,products.stock,categories.name as category FROM products JOIN categories ON category_id = categories.id""")
    products = cursor.fetchall()
    conn.close()
    return [dict(p) for p in products]


def add():
    try:
        name = (entry_name.get())
        if not name:
         messagebox.showwarning("Warning", "Product name can't be empty")
         return
        price = float(entry_price.get())
        stock = int(entry_stock.get())
        category = entry_category.get()
        add_products(name,price,stock,category)
        refresh_list()
    except ValueError:
        messagebox.showerror("Invalid", "Price must be a number and stock must be an integer")
def add_cat():
    name = entry_category.get()
    if not name:
        messagebox.showwarning("Warning", "Enter a category name")
        return
    add_category(name)
    status.config(text=f"✓ Category '{name}' added", fg="#00e5a0")
def delete():
    name = entry_name.get()
    if not name:
        messagebox.showwarning("Warning", "Enter a product name first")
        status.config(text="✗ Enter a product name", fg="#ff6a6a")
        return
    if not messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{name}'?"):
       return
       
    conn = sqlite3.connect("store.db")
    cursor =  conn.cursor()
    cursor.execute("DELETE FROM products WHERE LOWER(name) = LOWER(?)",(name,))
    conn.commit()
    conn.close()
    clear_entries()
    if cursor.rowcount == 0:
        messagebox.showwarning("Not Found", f"Product '{name}' doesn't exist")
    else:
     status.config(text=f"✓ {name} deleted", fg="#00e5a0")
     refresh_list()
def search():
    name = entry_name.get()
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE LOWER(name) = LOWER(?)",(name,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        result = dict(result)
        status.config(text=f"Found: {result['name']} - S/ {result['price']} - Stock: {result['stock']} - Category: {result['category_id']}",
            fg="#00e5a0")
    else :
       status.config(text="✗ Product not found", fg="#ff6a6a") 
def update():
    try:
        name = entry_name.get()
        if not name:
            messagebox.showwarning("Warning", "Enter a product name first")
            return
        new_stock = int(entry_stock.get())
        conn = sqlite3.connect("store.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE products SET stock = ? WHERE LOWER(name) = LOWER(?)",(new_stock,name))
        conn.commit()
        if cursor.rowcount == 0:
         messagebox.showwarning("Not Found", f"Product '{name}' doesn't exist")
         status.config(text="✗ Product not found", fg="#ff6a6a")
        else:
         status.config(text=f"✓ Stock updated for {name}", fg="#00e5a0")
         refresh_list()
        conn.close()
    except ValueError:
        messagebox.showerror("Invalid Input", "Stock must be a whole number")
        status.config(text="✗ Invalid stock value", fg="#ff6a6a")
def get_by_categories(category_name):
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""SELECT products.id,products.name,products.price,products.stock,products.category_id , categories.name as category FROM products JOIN categories ON products.category_id = categories.id WHERE LOWER(categories.name) = LOWER(?)""",(category_name,))
    products = cursor.fetchall()
    conn.close()
    return [dict(p)  for p in products]
def filter_by_category():
    category = entry_category.get()
    if not  category:
        refresh_list()
        return
    for row in tree.get_children():
        tree.delete(row)
    for p in get_by_categories(category):
        tree.insert("","end" ,values=(p['id'],p['name'],p['price'], p["stock"], p["category"]))
    status.config(text=f"Showing: {category}" , fg="#00e5a0")







create_table()
root = tk.Tk()
root.title("Storage Manager Plus")
root.configure(bg="#1e1e2e")
root.geometry("600x400")
top = tk.Frame(root,bg="#1e1e2e")
top.pack(pady=10)
tk.Label(top, text="Name" , bg="#1e1e2e" ,fg="white").grid(row=0,column=0,padx=5)
tk.Label(top, text="Price" , bg="#1e1e2e" ,fg="white").grid(row=0,column=1,padx=5)
tk.Label(top, text="Stock" , bg="#1e1e2e" ,fg="white").grid(row=0,column=2,padx=5)
tk.Label(top , text="Category" , bg="#1e1e2e" ,fg="white").grid(row=0,column=3 ,padx=5)
entry_name = tk.Entry(top,width=15)
entry_name.grid(row=1,column=0,padx=5)
entry_price = tk.Entry(top,width=15)
entry_price.grid(row=1,column=1,padx=5)
entry_stock = tk.Entry(top,width=15)
entry_stock.grid(row=1,column=2,padx=5)
entry_category = tk.Entry(top , width=15)
entry_category.grid(row=1,column=3,padx=5)
status = tk.Label(root,text="" ,bg="#1e1e2e",fg="#00e5a0")
status.pack(padx=5)
button_frame = tk.Frame(root,bg="#1e1e2e")
button_frame.pack(pady=5)
Button_add = tk.Button(button_frame,text="Add" , command=add ,  bg="#7c6aff", fg="white", width=12)
Button_add.pack(side="left",padx=4)
Button_delete = tk.Button(button_frame,text = "Delete", command=delete  ,bg="#54a0ff", fg="white", width=12)
Button_delete.pack(side="left" , padx=4)
Button_search = tk.Button(button_frame,text = "Search", command=search  ,bg="#ff9f43", fg="white", width=12)
Button_search.pack(side="left" , padx=4)
Button_upgrade = tk.Button(button_frame,text = "Upgrade", command=update  ,bg="#ff6a6a", fg="white", width=12)
Button_upgrade.pack(side="left" , padx=4)
Button_category = tk.Button(button_frame, text="Add Category", command=add_cat, bg="#00c896", fg="white", width=12)
Button_category.pack(side="left",padx=4)
Button_filter_by_category = tk.Button(button_frame,text="Filter Category", command=filter_by_category,bg="#ffd32a", fg="black", width=12)
Button_filter_by_category.pack(side="left",padx=4)
tree = ttk.Treeview(root , columns=("id","name" , "price" , "stock","category"), show="headings")
tree.heading("id",text="ID")
tree.heading("name",text="Name")
tree.heading("price",text="Price")
tree.heading("stock",text="Stock")
tree.heading("category",text="Category")
tree.column("id", width=40)
tree.column("name", width=150)
tree.column("price", width=100)
tree.column("stock", width=80)
tree.column("category", width=120)
tree.pack(padx=10,pady=10)
def clear_entries():
    entry_name.delete(0,tk.END)
    entry_price.delete(0,tk.END)
    entry_stock.delete(0,tk.END)
    entry_category.delete(0,tk.END)
def on_selected(event):
    selected = tree.focus()
    if  selected:
        values = tree.item(selected)["values"]
        entry_name.delete(0,tk.END)
        entry_name.insert(0,values[1])
        entry_price.delete(0,tk.END)
        entry_price.insert(0,values[2])
        entry_stock.delete(0,tk.END)
        entry_stock.insert(0,values[3])
        entry_category.delete(0,tk.END)
        entry_category.insert(0,values[4])
tree.bind("<<TreeviewSelect>>",on_selected)








def refresh_list():
    for row in tree.get_children():
        tree.delete(row)
    for p in get_all_products():
        tree.insert("","end",values=(p["id"],p["name"],p["price"],p["stock"],p["category"]))
refresh_list()
root.mainloop()
