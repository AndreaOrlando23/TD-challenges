import os


class DataCleaning:

    def __init__(self, fname, path=""):
        self.fname = fname
        self.path = path


    def get_path(self):
        # manage if user want different path
        if self.path == "":
            current_path = os.getcwd()  # get current working directory
            files_directory = os.path.join(current_path, "cases")  # d1 = d+\"cases"
            standard_path = os.path.join(files_directory, self.fname)
            return standard_path
        return self.path
    

    def read_file(self):
        path = self.get_path()
        with open(path, "r") as file:
            text = file.read()
            return text


    def read_only_500_lines(self):
        file = self.read_file()
        return file[:500]


    def frequency_of_values(self):
        '''
        Take a file and return a list of most frequent values.
        If the path is not specified, the program use the standard
        path passed from get_path() methods
        '''
        letters = {}

        file = self.read_file()
        for words in file:
            words = words.replace("\n", "").lower()
            for letter in words:
                letters[letter] = letters.get(letter, 0) + 1

        # build a list of values stored in letters{} ordered by the most frequent value 
        sorted_values = sorted(letters, key=letters.get, reverse=True)
        return sorted_values


    def only_letters(self):
        '''
        Get a list of values processed from frequency_of_values() methods
        and return a list of only alphabet letters
        '''
        list_of_values = self.frequency_of_values()
        list_of_letters = [letter for letter in list_of_values if letter.isalpha()]
        return list_of_letters[0] # return only the most frequent letter finded


# TEST
def main():

    FNAME1 = "Shakespeare-Hamlet.txt"
    FNAME2 = "Shakespeare-Macbeth.txt"
    FNAME3 = "Shakespeare-Romeo-And-Juliet.txt"

    PATH_FNAME2 = ".\Shakespeare-Macbeth.txt"

    test1 = DataCleaning(FNAME1)
    test2 = DataCleaning(FNAME2, PATH_FNAME2)
    test3 = DataCleaning(FNAME3)

    print(test1.only_letters())
    # print(test2.only_letters())
    # print(test3.only_letters())

    print(test1.read_only_500_lines())

    # print(test3.read_file())

if __name__ == "__main__":
    main()


