from random_word import RandomWord

class Поле_Чудес:
    def __init__(self, word_list, max_attempts=7):
        self.word = RandomWord(word_list).get_random_word()
        self.max_attempts = max_attempts
        self.attempts = 0
        self.guesses = set()
        self.display_word = ['_'] * len(self.word)

    def display(self):
        return ' '.join(self.display_word)

    def make_guess(self, letter):
        if letter in self.guesses:
            return "Вы угадали буква была: {letter}"

        self.guesses.add(letter)

        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.display_word[i] = letter

            if ''.join(self.display_word) == self.word:
                return "Поздравляю вы угадали! Слово было: " + self.word
            else:
                return "Красавчик ты угадал!"
        else:
            self.attempts += 1
            if self.attempts >= self.max_attempts:
                return "Игра окончена! Слово было: " + self.word
            else:
                return "Попробуй снова. У тебя осталось {} попыток.".format(self.max_attempts - self.attempts)

