# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
# 2. Добавить в класс Computer приватный метод make_computations, в котором бы выполнялись арифметические вычисления(‘+’,  ‘-’,  ‘*’,  ‘/’ ) с атрибутами объекта cpu и memory результат вывести красиво с помощью ‘ f ’ .
# 3. Добавить сеттеры и геттеры к существующим атрибутам и методу.
# class A:
#     def __init__(self):
#         pass

# class Computer:
#     def __init__(self, cpu, memory, RAM):
#         self.__cpu = cpu 
#         self.__memory = memory
#         self.ram = RAM
#     def __make_computations(self):
#         a = int(input("Введите первое число:"))
#         b = int(input("Введите второе число:"))
#         print(f"Результат сложения - ",a + b)
#         print(f"Результат вычитания - ",a - b)
#         print(f"Результат деления - ",a / b)
#         print(f"Результат умножения - ",a * b)
#     @property
#     def self_cpu(self):
#         return(self.__cpu)
#     @self_cpu.setter
#     def self_cpu(self, new_cpu):
#         self.__cpu = new_cpu
#     @property
#     def self_memory(self):
#         return(self.__memory)
#     @self_memory.setter
#     def self_memory(self, new_memory):
#         self.__memory = new_memory
#     @property
#     def self_make_computations(self):
#         return(self.__make_computations)
#     @self_make_computations.setter
#     def self_make_computations(self, new_make_computations):
#         self.__make_computations = new_make_computations
# computer = Computer("AMD Ryzen 5 5500U",512,8)

# # 4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
# # 5. Добавить сеттеры и геттеры к существующему атрибуту.
# # 6. Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты (например: если при вызове метода передать число 1 и номер телефона, распечатывается текст “Идет звонок на номер +996 771 24 47 45” с сим-карты-1 - Beeline).
# # phone.call()
# class Phone:
#     def __init__(self, sim_cards_list, camera_mpx):
#         self.__sim_cards_list = sim_cards_list
#         self.camera_mpx = camera_mpx
#     @property
#     def self_sim_cards_list(self):
#         return(self.__sim_cards_list)
#     @self_sim_cards_list.setter
#     def sim_cards_list(self, new_sim_cards_list):
#         self.sim_cards_list = new_sim_cards_list
#     def call(self, call_to_number, sim_cards_number):
#         # call_to_number = int(input("Введите номер телефона:"))        
#         # sim_cards_number = int(input("Выберите сим карту(1 - Beeline, 2 - O!):"))
#         if sim_cards_number == "1":
#             print("Идет звонок на номер +996",call_to_number,"с сим-карты-1 - Beeline")
#         elif sim_cards_number == "2":
#             print("Идет звонок на номер +996",call_to_number,"с сим-карты-2 - O!")        
#         else:
#             print("Ошибка!!!")
# phone = Phone({1 == "O!", 2 == "Beeline"}, 12)
# phone.call(input("Введите номер телефона:"),input("Выберите сим карту(1 - Beeline, 2 - O!):"))

# # 7. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
# # 8. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал симуляцию проложения маршрута до локации.
# # 9. Добавить в класс SmartPhone метод add_memeory_card который бы увеличивал память телефона
# class SmartPhone(Computer, Phone):
#     def __init__(self, cpu, memory, sim_cards_list, camera_mpx):
#         Computer.__init__(self, cpu, memory, RAM = self.ram)    
#         Phone.__init__(self, sim_cards_list, camera_mpx = self.camera_mpx)
#         self.memory = memory
#         self.cpu = cpu 
#     def use_gps(self, location):
#         a = int(input("Если хотите включить location(1 = да, 2 = нет):"))
#         if a == 1:
#             print("Функция включена",f"Результат -",location)
#         elif a == 2:
#             print("Функция location отключена")
#         else:
#             print("Ошибка!!!")
#     def add_memeory_card(self):
#         add_memeory_card1 = int(input("Введите на сколько вы хотите увеличить память:"))
#         print("Память =",self.memory + add_memeory_card1,"Gb")
#     def info(self):
#         print("В камере телефона -",self.camera_mpx,"mpx")
#         print("Процессор -",self.cpu)
#         print("Памяти на компьютере -",self.memory,"Гб")
#         print("Оперативной памяти на компьютере -",self.ram,"Гб")
# smartphone = SmartPhone("AMD Ryzen 5 5500U",512,{1 == "O!", 2 == "Beeline"})
# smartphone.use_gps("Татьяна 200 м от вас!")
# smartphone.info()


# 10. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
# Задание выполнено 
# 11. Распечатать информацию о созданных объектах с помощью метода info
# Задание выполнено
# 12. Опробовать все возможные методы каждого объекта
# Задание выполнено

