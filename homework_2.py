# 1. Создать класс Person с атрибутами fullname, age, is_married

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

# 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке

# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married
#     def introduce_myself(self):
#         print(self.fullname)
#         print(self.age)
#         print(self.is_married)

# 3. Создать класс Student наследовать его от класса Person и дополнить его методом average_value который запрашивал бы словарь, где ключ это название урока, а значение - оценка. Этот метод должен подсчитывать среднюю оценку ученика по всем предметам.

# class Student(Person):
#     def __init__(self, fullname, age, is_married):
#         super().__init__(fullname, age, is_married)
#         Baki = [5,5,5,3,4,2,3]
#     def average_value(self):
#         Baki = [5,5,5,3,4,2,3]
#         average_value1 = input("Введите название вашей ячейки что бы мы дали вам информацию - ")
#         if average_value1 == "Baki":
#             print("Ваша средняя оценка - ",sum(Baki)/len(Baki))
# student = Student("Bakai", 14, "False")
# student.average_value()
        
# 4. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.

# class Teacher(Person):
#     def __init__(self, fullname, age, is_married, experience = 0):
#         super().__init__(fullname, age, is_married)
#         self.experience = experience

# 5. Добавить в класс Teacher атрибут класса salary

# class Teacher(Person):
#     def __init__(self, fullname, age, is_married, experience = 0, salary = 0):
#         super().__init__(fullname, age, is_married)
#         self.experience = experience
#         self.salary = salary

# 6. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 3000 за каждый год опыта.

# class Teacher(Person):
#     def __init__(self, fullname, age, is_married, experience, salary):
#         super().__init__(fullname, age, is_married)
#         self.experience = experience
#         self.salary = salary
#     def salary_increase_due_to_experience(self):
#         print(self.salary + (self.experience * 3000))

# teacher = Teacher("Bakai", 14, "No", 5, 30000)
# teacher.salary_increase_due_to_experience()

# 7. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату

# class Teacher(Person):
#     def __init__(self, fullname, age, is_married, experience, salary):
#         super().__init__(fullname, age, is_married)
#         self.experience = experience
#         self.salary = salary
#     def salary_increase_due_to_experience(self):
#         self.salary + (self.experience * 3000)
#         print("Зарплата учителя -",self.salary)
#     def info(self):
#         print("Имя преподавателя - ",self.fullname)
#         print("Возраст преподавателя - ",self.age,"лет")
#         print("Состоит в браке/Не состоит в браке - ",self.is_married)

# teacher = Teacher("Bakai", 14, "False", 5, 30000)
# teacher.salary_increase_due_to_experience()
# teacher.info()

# 8. Создать объект студента и распечатать всю информацию о нем и вывести среднюю оценку

# class Student(Person):
#     def __init__(self, fullname, age, is_married,Baki):
#         super().__init__(fullname, age, is_married)
#         self.Baki = Baki
#     def average_value(self):
#         average_value1 = input("Введите название вашей ячейки что бы мы дали вам информацию - ")
#         if average_value1 == "Baki":
#             sum(self.Baki)/len(self.Baki)
#     def info(self):
#         print("Имя студента - ",self.fullname)
#         print("Возраст студента - ",self.age)
#         print("Состоит в браке/Не состоит в браке - ",self.is_married)
#         print("Средняя оценка ученика - ",sum(self.Baki)/len(self.Baki))
# student = Student("Bakai", 14, "False",[5,5,5,3,4,2,3])
# student.info()