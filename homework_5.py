# Создайте игру на Python с использованием ООП и декомпозицией:

# Игровой процесс:

# Игра начинается с приветственного сообщения и выбора случайного слова
# Игроку предоставляется ограниченное количество попыток (например, 7).
# Игрок вводит буквы одну за другой. Если буква угадана, она отображается на экране. Если буква не угадана, количество попыток уменьшается.
# Игра продолжается, пока игрок не угадает слово полностью или не исчерпает все попытки.
# Игроку сообщается о победе или поражении, а также показывается загаданное слово.
# Разделите игру на модули:
# Можете разделить по своему желанию, так же количество модулей не ограничено
while True:
    class Game:
        def Welcome():
            print("Добро пожаловать в Игру!!!")
            print("Правила игры - Игроку предоставляется ограниченное количество попыток (например, 7).Игрок вводит буквы одну за другой. Если буква угадана, она     отображается на экране. Если буква не угадана, количество попыток уменьшается. Игра продолжается, пока игрок не угадает слово полностью или не исчерпает     все попытки. Игроку сообщается о победе или поражении, а также показывается загаданное слово.")
    
        def game_1():
            player_health = 7
            dict_1 = {"Р","а","н","д","о","м"}
            player_choice = input("Введите первую букву:")
            if player_choice == (dict_1):
                print("Вы угадали первую букву!!!")
            # elif player_choice == (dict_1[2]):
            #     print("Вы угадали вторую букву!!!")
            # elif player_choice == (dict_1[3]):
            #     print("Вы угадали вторую букву!!!")
            # elif player_choice == (dict_1[4]):
            #     print("Вы угадали вторую букву!!!")
            # elif player_choice == (dict_1[5]):
            #     print("Вы угадали вторую букву!!!")
            # elif player_choice == (dict_1[6]):
            #     print("Вы угадали вторую букву!!!")
            else:
                player_health - 1
                print("У вас осталось",player_health,"попыток")
    game = Game
    game.Welcome()
    game.game_1()
        
        
# Доп дз(не обязательно!):

# Попробуйте добавить в игру что то своё

# Или можете создать свою игру , но обязательно разделите код по модулям

# Примечание:

# Убедительная просьба не пользоваться chatGPT в целях выполнения домашних работ
# Но можно использовать ИИ в целях развития своих знаний или для идей с игрой
# Если возникнут проблемы с выполнением домашних работ не стесняйтесь писать мне или менторам
#  git remote add origin https://github.com/Baki2009/Bakai2.0