# TODO

def most_common_bit(binary_list):
    gamma = ''
    epsilon = ''
    index = 0
    for bit in binary_list:
        print(bit)
        print(bit[index])
        common1 = 0
        common0 = 0
        if bit[index] == '1':
            common1 += 1
        else:
            common0 += 1

        if common1 > common0:
            gamma += '1'
        else:
            epsilon += '0'
        
        index += 1
        if index == len(bit):
            break
    
    return [gamma, epsilon]



with open('test-input.txt') as file:
    positions = [val for val in file.read().split()]


print(most_common_bit(positions))