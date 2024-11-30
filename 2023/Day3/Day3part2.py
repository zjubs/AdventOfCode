
import re
import math

coord_numbers = {}
coord_symbol = {}
numbers = {}

line_num = 0

with open('XmasOfCode2023/Day3/Day3Input.txt', 'r') as file:
    for line in file:

        digit_matches = [(match.start(), match.end()) for match in re.finditer(r'\d+', line)]
        # find *
        symbol_positions = [match.start() for match in re.finditer(r'\*', line)]
        coord_numbers[str(line_num)] = digit_matches
        numbers[str(line_num)] = [int(line[number[0]:number[1]]) for number in digit_matches]

        coord_symbol[str(line_num)] = symbol_positions

        line_num += 1


# find all valid cells around * 
gears ={}
for row in coord_symbol.keys():
    for col in coord_symbol[row]:
        valid_cells = []
        for i in range(-1,2):
            for j in range(-1,2):
                 #print(f'i,j:{i},{j}')
                 tuple_coord = (int(row)+ i,col + j)
                 valid_cells.append(tuple_coord)
        gears[(int(row),col)] = valid_cells



gear_nums = {}

for row in coord_numbers.keys():
    for index,occurence in enumerate(coord_numbers[row]):
        coords = [(int(row),position) for position in range(occurence[0],occurence[1])]
        for key,val in gears.items():
            valid_num = any(coord in val for coord in coords)
            if valid_num:
                # Use setdefault to add the value to the list
                gear_nums.setdefault(key, []).append(numbers[row][index])

print(gear_nums)

#calc answer but only include values if there are 2 values around the gear/*
result_part2 = 0 
for val in gear_nums.values():
    if len(val) == 2:
        result_part2 += math.prod(val)

print(result_part2)




#is_present = all(coord in coordinate_list for coord in test_coordinates)



# for row in coord_numbers.keys():
#     for coord in row:
#         for i in range(-1,1):
#             if 

