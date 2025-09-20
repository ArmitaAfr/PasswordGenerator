import random
import string
from abc import ABC, abstractmethod

import nltk 

nltk.download('words')


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class pinGenerator(PasswordGenerator):
    def __init__(self, length):
        self.length = length

    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(8)])


class RandsomPasswordGenerator(PasswordGenerator):
    def __init__(self, length=8, include_numbers=False, include_symbols=False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        return ''.join([random.choice(self.characters) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self, 
        number_of_words: int = 4, 
        seperator: str = '-', 
        capitalize: bool = False, 
        vocabulary: list = None
    ):
        if vocabulary is None:
            self.vocabulary = nltk.corpus.words.words()

        self.num_of_words = number_of_words
        self.seperator = seperator
        self.capitalize = capitalize


    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalize:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
        return self.seperator.join(password_words)

if __name__ == "__main__":
    pin_gen = pinGenerator(length=8)
    print("PIN:", pin_gen.generate())

    rand_gen = RandsomPasswordGenerator(length=12, include_numbers=True, include_symbols=True)
    print("Random password:", rand_gen.generate())

    mem_gen = MemorablePasswordGenerator(number_of_words=4, seperator='-', capitalize=True)
    print("Memorable password:", mem_gen.generate())


