'''
Write a function that take a natural number and a base
return the number in the specific base passed
'''

def decimal_to_base(number, base):
    quotient = number//base
    reminder = f'{number % base}'
    if quotient == 0:
        return reminder
    else:
        reminder += decimal_to_base(quotient, base)
    
    return reminder


def reverse_string(string):
    return ''.join(reversed(string))


def main():
    num = int(input("Enter a number: "))
    base = int(input("Enter the base: "))
    computation = decimal_to_base(num, base)

    result = reverse_string(computation)
    
    print(f"The conversion of {num} in base {base} is: {result}")


if __name__ == '__main__':
    main()
