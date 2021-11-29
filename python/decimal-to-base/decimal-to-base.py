'''
Write a function that take a natural number and a base
return the number in the specific base passed
'''

def decimal_to_base(number, base):
    operation = number//base
    reminder = f'{number % base}'
    if operation == 0:
        return reminder
    else:
        reminder += decimal_to_base(operation, base)
    
    return reminder


def main():
    num = int(input("Enter a number: "))
    base = int(input("Enter the base: "))
    result = ''.join(reversed(decimal_to_base(num, base)))
    
    print(f"The conversion of {num} in base {base} is: {result}")


if __name__ == '__main__':
    main()
