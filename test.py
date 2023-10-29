# 1. Создайте класс Person. В конструкторе он принимает name, surname, age.
# атрибут name должен быть приватным
# атрибут surname должен быть защищенным
# Создайте метод info, который возвращает name, surname, age. Создайте 3 экземпляра класса и вызовите методы.
# class Person:
#     def __init__(self, name, surname, age):
#         self.__name = name 
#         self._surname = surname
#         self.age = age 
    
#     def info(self):
#         print(f"Имя - {self.__name}, Фамилия - {self._surname}, Возраст - {self.age}")
# person1 = Person("Bakai","Samatov",14)
# person2 = Person("Bakzat","Beishenaliev",16)
# person3 = Person("Syrgak","Samatov",20)

# person1.info()
# person2.info()
# person3.info()
# 2. Напишите класс Math. Используйте внутри класса магические методы __add__ и __sub__ для сложения и вычитания. После того вы все сделали, создайте экземпляр класса и выведите значения из класса
# class Math:
#     def __init__(self, first_num):
#         self.first_num = first_num

#     def __add__(self, other):
#         return Math(self.first_num + other.first_num)

#     def __sub__(self, other):
#         return Math(self.first_num - other.first_num)

# math = Math(10)

# result_add = math + Math(5)
# result_sub = math - Math(3)

# print("Сложение:", result_add.first_num)  
# print("Вычитание:", result_sub.first_num) 

# Напишите класс Сonstructor, которое имитирует строительство жилого дома. В конструкторе мы передаем сколько этажей мы хотим построить. Затем делаем метод build, который строит наш дом пока мы не дойдем до этажа которую мы хотим построить. И также создайте магический метод __str__, для выведение данных нашего класса

# class Constructor:
#     def __init__(self, total_floors):
#         self.total_floors = total_floors
#         self.built_floors = 0

#     def build(self):
#         if self.built_floors < self.total_floors:
#             self.built_floors += self.total_floors
#             print(f"Построено этажей - {self.built_floors}")
#         else:
#             print("Дом уже построен")

#     def __str__(self):
#         return f"Построено - {self.built_floors} из {self.total_floors} этажей"

# builder = Constructor(5)
# builder.build()
# print(builder)

# import sqlite3

# connect = sqlite3.connect("bank.db")
# cursor = connect.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS persons(
#                id INTEGER PRIMARY KEY,
            #    name VARCHAR(100) NOT NULL,
            #    surname VARCHAR(100) NOT NULL,
            #    age INTEGER NOT NULL
# );
# """)

    
# class Person:
#     def __init__(self, name, surname, age):
#         self.__name = name 
#         self._surname = surname 
#         self.age = age 

#     @property
#     def self_name(self):
#         return(self.__name)
#     @self_name.setter
#     def self_name(self, new_name):
#         self.__name = new_name

#     def add(self, name, surname, age, email):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         cursor.execute(f"""INSERT INTO persons (name, surname, age, email, balance, props, is_active)
#                        VALUES ('{name}', '{surname}', '{age}');""")
        
#         connect.commit()
        
#     # def add(self, __name, _surname, age):
#     #     self.name = __name
#     #     self.surname = _surname
#     #     self.age = age
#     #     cursor.execute(f"""INSERT INTO persons (name, surname, age)
#     #                 VALUES ('{__name}', '{_surname}', '{age}'""")
#     #     connect.commit()

    # def info(self):
    #     print(f"Имя - {self.__name}, Фамилия - {self._surname}, Возраст - {self.age}")

#     def main(self):
#         print()

# person1 = Person("Bakai","Samatov",14)
# person2 = Person("Bakzat","Beishenaliev",16)
# person3 = Person("Syrgak","Samatov",20)

# person1.info()
# person2.info()
# person3.info()

# connect.commit()
# connect.close()

import sqlite3

conn = sqlite3.connect('persons.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS persons (
        id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            surname VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL
    )
''')
conn.commit()

class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self._surname = surname
        self.age = age

    def info(self):
        print(f"Имя - {self.__name}, Фамилия - {self._surname}, Возраст - {self.age}")

    def add_to_database(self):
        conn = sqlite3.connect('persons.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO persons (name, surname, age) VALUES (?, ?, ?)', (self.__name, self._surname, self.age))
        conn.commit()
        conn.close()

person1 = Person("Bakai","Samatov",14)
person2 = Person("Bakzat","Beishenaliev",16)
person3 = Person("Syrgak","Samatov",20)

person1.info()
person2.info()
person3.info()

person1.add_to_database()
person2.add_to_database()
person3.add_to_database()

conn.close()
