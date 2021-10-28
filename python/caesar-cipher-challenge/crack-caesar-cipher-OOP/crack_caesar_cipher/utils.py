import os


FNAME1 = "Shakespeare-Hamlet.txt"
FNAME2 = "Shakespeare-Macbeth.txt"
FNAME3 = "Shakespeare-Romeo-And-Juliet.txt"

def get_path(fname):
    current_path = os.getcwd()  # get current working directory
    files_directory = os.path.join(current_path, "cases")  # d1 = d+\"cases"
    path = os.path.join(files_directory, fname)
    return path


def letter_frequency(text):
    try:
        fname = get_path(text)
        letters = {}
        with open(fname, "r") as file:
            for words in file:
                words = words.replace("\n", "").lower()
                for letter in words:
                    letters[letter] = letters.get(letter, 0) + 1

            # build a list of values stored in letters{} ordered by the more frequent 
            sorted_values = sorted(letters, key=letters.get, reverse=True)
            print(sorted_values)

    except IOError:
        print("Errors while accessing the file.")

letter_frequency(FNAME1)
print()
letter_frequency(FNAME2)
print()
letter_frequency(FNAME3)

