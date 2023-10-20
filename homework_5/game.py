from ПолеЧудес import Поле_Чудес

word_list = ["апельсин", "пельмени", "машина", "виноград", "космос", "чайник", "ноутбук"]
game = Поле_Чудес(word_list)

print("Добро пожаловать в игру Поле чудес!")
print("Слово которое нужно угадать:" + game.display())

while game.attempts < game.max_attempts:
    guess = input("Угадай букву: ").lower()
    result = game.make_guess(guess)
    print(result)
    print("Слово: " + game.display())

print("Игра окончена. Слово было: " + game.word)

