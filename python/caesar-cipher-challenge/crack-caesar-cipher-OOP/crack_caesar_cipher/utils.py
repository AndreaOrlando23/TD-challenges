

def check_input(answer):
    if answer == "y":
        return True
    return False


def ask_user():
    answer = input("y/n: ")
    if check_input(answer):
        return answer
    return False

def return_first_value(list_of_values):
    return list_of_values[0]


def iterate_each_value(list_of_values):
    return_first_value(list_of_values)
    for value in list_of_values:
        if ask_user():
            return value
        break
    return value
    

def main():
    test = ask_user()

    iter = iterate_each_value([1,2,3,4,5])
    print(iter)

main()
