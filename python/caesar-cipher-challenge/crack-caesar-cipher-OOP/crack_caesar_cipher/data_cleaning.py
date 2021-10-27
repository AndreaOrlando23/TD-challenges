import os


class DataCleaning:

    def __init__(self, fname):
        self.fname = fname


    def get_standard_path(self):
        current_path = os.getcwd()  # get current working directory
        files_directory = os.path.join(current_path, "cases")  # d1 = d+\"cases"
        path = os.path.join(files_directory, self.fname)
        return path


    def frequency_of_values(self, path=""):
        letters = {}

        # manage if user want different path of standard sub directory
        if path == "":
            path = self.get_standard_path()

        with open(path, "r") as file:
            for words in file:
                words = words.replace("\n", "").lower()
                for letter in words:
                    letters[letter] = letters.get(letter, 0) + 1

            # build a list of values stored in letters{} ordered by the more frequent 
            sorted_values = sorted(letters, key=letters.get, reverse=True)
            return sorted_values


    def only_letters(self):
        pass




FNAME1 = "Shakespeare-Hamlet.txt"
FNAME2 = "Shakespeare-Macbeth.txt"
FNAME3 = "Shakespeare-Romeo-And-Juliet.txt"

test = DataCleaning(FNAME1)

print(test.frequency_of_values())


