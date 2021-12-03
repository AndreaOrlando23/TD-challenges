
def planned_positions(commands):
    trip_plan = {'forward': 0, 'down': 0, 'up': 0, 'aim': 0, 'depth': 0}

    for position in range(len(commands)):

        if commands[position] in trip_plan:
            trip_plan[commands[position]] += int(commands[position+1])

            if commands[position] == 'down':
                trip_plan['aim'] += int(commands[position+1])
            elif commands[position] == 'up':
                trip_plan['aim'] -= int(commands[position+1])
            elif commands[position] == 'forward':
                trip_plan['depth'] += (trip_plan['aim'] * int(commands[position+1]))
    
    
    return trip_plan


with open('data.txt') as file:
    positions = [val for val in file.read().split()]


data = planned_positions(positions)
print(data)

final_horizontal = data['forward']
final_depth = data['down'] - data['up']

solution_part_1 = final_horizontal * final_depth
solution_part_2 = data['forward'] * data['depth']

print(f'PART 1 Dive - Solution: {solution_part_1}')
print(f'PART 2 Dive - Solution: {solution_part_2}')


