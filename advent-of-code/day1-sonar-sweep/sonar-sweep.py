def num_increases(data):
    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            count += 1
    
    return count


with open('data.txt') as file:
    values = [int(val) for val in file.read().split()]

        
print(f'PART1 Sonar Sweep - Number of increases: {num_increases(values)}')


three_measurement = []

for i in range(2, len(values)):
    three_measurement.append(values[i] + values[i-1] + values[i-2])

print(f'PART2 Sonar Sweep - Number of increases: {num_increases(three_measurement)}')
