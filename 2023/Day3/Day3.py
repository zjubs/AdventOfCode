
import re
# get coord of numbers
# get coords of symbols

# then compare

coord_numbers = {}
coord_symbol = {}
numbers = {}

line_num = 0

with open('XmasOfCode2023/Day3/Day3Input.txt', 'r') as file:
    for line in file:
        #digit_matches = [(match.start(), match.end() - 1) for match in re.finditer(r'\d+', line)]
        digit_matches = [(match.start(), match.end()) for match in re.finditer(r'\d+', line)]
        # find non . and non digits and non newlinw
        symbol_positions = [match.start() for match in re.finditer(r'[^.\d\n]', line)]
        #print(digit_matches)
        #print(symbol_positions)
        coord_numbers[str(line_num)] = digit_matches
        numbers[str(line_num)] = [int(line[number[0]:number[1]]) for number in digit_matches]

        coord_symbol[str(line_num)] = symbol_positions

        line_num += 1


# find all valid cells
valid_cells = []
for row in coord_symbol.keys():
    for col in coord_symbol[row]:
        for i in range(-1,2):
            for j in range(-1,2):
                 #print(f'i,j:{i},{j}')
                 tuple_coord = (int(row)+ i,col + j)
                 valid_cells.append(tuple_coord)

#print(valid_cells)

#print(coord_numbers)
# find all number in valid cells
result_part1 = 0 
for row in coord_numbers.keys():
    for index,occurence in enumerate(coord_numbers[row]):
        coords = [(int(row),position) for position in range(occurence[0],occurence[1])]
        valid_num = any(coord in valid_cells for coord in coords)
        if valid_num:
            result_part1 += numbers[row][index]

print(result_part1 )




#is_present = all(coord in coordinate_list for coord in test_coordinates)



# for row in coord_numbers.keys():
#     for coord in row:
#         for i in range(-1,1):
#             if 

