import random

class RandomWord:
    def __init__(self, word_list):
        self.word_list = word_list

    def get_random_word(self):
        return random.choice(self.word_list)






        
