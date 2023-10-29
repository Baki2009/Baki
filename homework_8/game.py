import random
from player import Player
from database import RPSDatabase

class RPSGame:
    def __init__(self, db_name):
        self.database = RPSDatabase(db_name)

    def play_game(self):
        print("Добро пожаловать в игру 'Камень, Ножницы, Бумага'!")

        player_name = input("Введите ваше имя: ")
        player = Player(player_name)

        while True:
            player_choice = player.get_choice()
            computer_choice = random.choice(["камень", "ножницы", "бумага"])
            result = self.determine_winner(player_choice, computer_choice)
            self.database.save_result(player_name, player_choice, computer_choice, result)
            print(f"Вы выбрали {player_choice}, компьютер выбрал {computer_choice}. Результат: {result}")

            play_again = input("Хотите сыграть еще раз? (да/нет): ")
            if play_again.lower() == "да":
                break
            
    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Ничья"
        elif (player_choice == "камень" and computer_choice == "ножницы"):
            print("Вы выиграли!") 
        elif (player_choice == "ножницы" and computer_choice == "бумага"):
            print("Вы выиграли!")
        elif (player_choice == "бумага" and computer_choice == "камень"):
            print("Вы выиграли!")
        else:
            return "Компьютер выиграл"

if __name__ == "__main__":
    game = RPSGame("rps.db")
    game.play_game()
