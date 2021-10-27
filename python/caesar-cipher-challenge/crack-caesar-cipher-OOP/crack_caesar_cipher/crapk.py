from operator import itemgetter
import os


FNAME1 = "Shakespeare-Hamlet.txt"
FNAME1 = "Shakespeare-Macbeth.txt"
FNAME1 = "Shakespeare-Romeo-And-Juliet.txt"

def get_file(fname):
    current_path = os.getcwd()  # get current working directory
    files_directory = os.path.join(current_path, "cases")  # d1 = d+\"cases"
    path = os.path.join(files_directory, fname)
    return path


def letter_frequency(text):
    try:
        fname = get_file(text)
        letters = {}
        with open(fname, "r") as file:
            for words in file:
                words = words.replace("\n", "").lower()
                for letter in words:
                    letters[letter] = letters.get(letter, 0) + 1

            print(sorted(letters.items(), key=itemgetter(1), reverse=True))

    except IOError:
        print("Errors while accessing the file.")

letter_frequency(FNAME1)




