with open('data.txt', 'r') as file:
    lines = file.read().split()
    print(lines)
    count = 0
    
    for i in range(1, len(lines)):
        if lines[i] > lines[i-1]:
            count += 1
               
        
    print(f'Measurement larger then previous measurement: {count}')
