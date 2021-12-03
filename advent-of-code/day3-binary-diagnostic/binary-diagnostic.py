# TODO

def binary_diagnostic(binary_list):
    gamma = ''
    epsilon = ''
    
    for bit in range(0, len(binary_list[0])):
        one = 0
        zero = 0
        for binary in range(0, len(binary_list)):
            if binary_list[binary][bit] == '0':
                zero += 1
            else:
                one += 1
            
        if zero > one:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    g = int(gamma, 2)
    e = int(epsilon, 2)
    
    return [g, e]



with open('data.txt') as file:
    binary_data = [val for val in file.read().split()]


data = binary_diagnostic(binary_data)
print(f'PART 1 Binary Diagnostic - Solution: {data[0]*data[1]}')
