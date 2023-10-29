import sqlite3

def create_database_and_table():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title VARCHAR (200) NOT NULL,
            price REAL NOT NULL DEFAULT 0.0,
            quantity INTEGER NOT NULL DEFAULT 0
        );"""
    )

    conn.commit()
    conn.close()

def add_product(product_title, price, quantity):

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (product_title, price, quantity)
        VALUES (?, ?, ?)
    ''', (product_title, price, quantity))
    conn.commit()
    conn.close()
    print("Продукт успешно добавлен в базу данных.")


create_database_and_table()

add_product("Новый продукт", 19.99, 10)

# Доп ДЗ:
# Добавить функцию, которая бы выбирала из БД товары которые дешевле 100 сомов и распечатывала бы их в консоли