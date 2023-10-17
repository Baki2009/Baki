# Задание 1:
# Создайте класс Fruits c атрибутами - (name, color, weight)
# Создайте три объекта класса и с помощью метода выведите информацию о каждом фрукте 

# class fruits():
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
    
#     def info(self):
#         print(f"Название фрукта: {self.name}, цвет фрукта: {self.color}, вес фрукта: {self.weight}")

# fruit1 = fruits("apple","red","176 gram")
# fruit2 = fruits("pear","green","150 gram") 
# fruit3 = fruits("orange","orange","180 gram")

# fruit1.info()
# fruit2.info()
# fruit3.info()

# Задание 2:
# Создайте класс Car c атрибутами - (model, year, color)
# Создайте метод drive с входящим параметром city(город) который будет выводить текст (Машина - `модель вашей машины`  едет в  - `ваш город`)

# class Car:
#     def __init__(self, model, year, color, city):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.drive = True
#         self.city = city

#     def info(self):
#         print(f"Бренд машины - {self.model}, год выпуска - {self.year}, цвет - {self.color}")
        
#     def cityy(self):
#         print("Машина -",{self.model} ,"едет в город -",{self.city})

# mercedes = Car("cls", 2020, "black", "Bishkek")
# mercedes.info()
# mercedes.cityy()

        
# Доп. Задание:
# Улучшите класс Car:
# Добавьте атрибут fuel со значением 0
# Добавьте метод refuel который будет пополнять бак и 	поставьте ограничение - (за раз можно пополнить 	только на 40 литров) 

# class Car:
#     def __init__(self, model, year, color, city):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.drive = True
#         self.city = city
#         self.fuel = 0
#         # self.refuel = False

#     def refuell(self):
#         gas_station = int(input("Введите сколько литров вы хотите заправить(Максимум 40 литров): "))

#         if gas_station > 40:
#             print("Максимум можно залить только 40 литров!!!")
#         elif gas_station < 1:
#             print("Минимум можно залить 1 литр")
#         elif self.fuel == 0:
#             self.fuel += gas_station
#             print("В бензобаке",{self.fuel},"литров")    
#         else:
#             print("Ошибка!!!")

#     def info_about_car(self):
#         print(f"Модель - {self.model}")
#         print(f"Год выпуска - {self.year}")
#         print(f"Цвет авто - {self.color}")
#         print(f"Бензина в бензобаке - {self.fuel} литров")

# mercedes = Car("cls", 2020, "black", "Bishkek")
# mercedes.info_about_car()
# mercedes.refuell()

# Измените метод drive :
# 	Теперь он должен запрашивать не только город но и 	расстояние до этого города, так же учитывайте что 	машина  расходует 1л / 10км. Если у машины не хватит 	бензина доехать, то должна появится надпись которая 	будет предупреждать сколько км может проехать 	машина 

# class Car:
#     def __init__(self,model,year,color,city,distance):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.city = city
#         self.fuel = 150
#         self.distance = distance
#     def info(self):
#         print(f"Модель - {self.model}")
#         print(f"Год выпуска - {self.year}")
#         print(f"Цвет авто - {self.color}")
#         print(f"Бензина в бензобаке - {self.fuel} литров")
#     def minus(self):
#         disatancee = self.distance / 10
#         if self.fuel < self.distance:
#             print("Не хватает топлива!!! Заправьте машину!!!")
#         elif self.fuel >= self.distance:
#             print("Машина едет")
#             self.fuel -= disatancee
#             print("Вы доехали!!! Бензина осталось",self.fuel,"литров")
#     def cityy(self):
#         a = input("Введите город в который вы едите: ")
#         print("Вы едите в город",a)                    

#     def refuell(self):
#         gas_station = int(input("Введите сколько литров вы хотите заправить(Максимум 40 литров): "))
#         if gas_station > 40:
#             print("Максимум можно залить только 40 литров!!!")
#         elif gas_station < 1:
#             print("Минимум можно залить 1 литр")
#         elif self.fuel == 0:
#             self.fuel += gas_station
#             print("В бензобаке",{self.fuel},"литров")    
#         else:
#             print("Ошибка!!!")
    
# mercedes = Car("cls", 2020, "black", "Bishkek",100)
# mercedes.info()
# mercedes.cityy() 
# mercedes.minus()