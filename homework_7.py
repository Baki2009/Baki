# Дз №7
# 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3
# 2. В БД создать таблицу products
# 3. В таблицу добавить поле id - первичный ключ, тип данных числовой и поддерживающий авто-инкрементацию.
# 4. Добавить поле product_title (название продукта) текстового типа данных максимальной длиной 200 символов, поле не должно быть пустым (NOT NULL)
# 5. Добавить поле price (цена продукта) не целочисленного (float) типа данных размером 10 цифр из которых 2 цифры поле плавающей точки, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0.0
# 6. Добавить поле quantity (количество продукта) целочисленного (int) типа данных, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0
# 7. Добавить функцию которая бы добавляла в БД продукты
# 8. Добавить функцию которая удаляет продукт по id

import sqlite3

def create_database_and_table():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
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