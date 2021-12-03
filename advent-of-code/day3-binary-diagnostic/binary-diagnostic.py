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
    data = [val for val in file.read().split()]
    
solution1 = binary_diagnostic(data)
print(f'PART 1 Binary Diagnostic - Solution: {solution1[0]*solution1[1]}')  # 1458194

data2 = data.copy()

index = 0
while len(data) > 1:
    one = 0
    zero = 0
    ones = []
    zeroes = []
    for c in range(0, len(data)):
        if data[c][index] == '0':
            zero += 1
            zeroes.append(data[c])
        else:
            one += 1
            ones.append(data[c])
    
    if zero > one:
        data = zeroes
    else:
        data = ones
    index += 1
    
oxygen = int(data[0], 2)


data = data2
index = 0
while len(data) > 1:
    one = 0
    zero = 0
    ones = []
    zeroes = []
    for c in range(0, len(data)):
        if data[c][index] == '0':
            zero += 1
            zeroes.append(data[c])
        else:
            one += 1
            ones.append(data[c])
    
    if one < zero:
        data = ones
    else:
        data = zeroes
    
    index += 1
    
co2 = int(data[0], 2)

solution2 = oxygen*co2
print(f'PART 2 Binary Diagnostic - Solution: {solution2}')  # 2829354
