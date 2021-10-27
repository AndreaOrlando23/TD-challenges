

def iterate_each_value(list_of_values):
    for value in list_of_values:
        return value


def check_input(answer):
    if answer == "y":
        return True
    return False

def main():
    test = input("y/n: ")
    list_of_values = [1, 2, 3, 4, 5]

    while check_input(test):
        for value in list_of_values:
            print(value)
            test = input("y/n: ")
            break



main()

