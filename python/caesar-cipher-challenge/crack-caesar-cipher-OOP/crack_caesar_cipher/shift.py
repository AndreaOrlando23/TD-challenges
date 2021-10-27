from data_cleaning import DataCleaning


FNAME1 = "Shakespeare-Hamlet.txt"

class Shift:

    # vowels in order of relative frequency in the English language
    # reference: https://en.wikipedia.org/wiki/Letter_frequency
    list_of_vowels = ["e", "a", "o", "i", "u", "y"]

    def __init__(self, list_of_letters):
        self.list_of_letters = list_of_letters

    
    def get_ascii_index(self):
        ascii_indexes = {}
        for letter in self.list_of_letters:
            ascii_indexes[letter] = ord(letter)
        return ascii_indexes





test = DataCleaning(FNAME1)
test1 = Shift(["e", "a", "o", "i", "u", "y"])

print(test1.get_ascii_index())