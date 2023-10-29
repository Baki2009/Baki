class Player:
    def __init__(self, name):
        self.name = name

    def get_choice(self):
        while True:
            choice = input(f"{self.name}, выберите (камень, ножницы, бумага): ")
            if choice in ("камень", "ножницы", "бумага"):
                return choice
            else:
                print("Неверный выбор. Пожалуйста, выберите (камень, ножницы, бумага).")
