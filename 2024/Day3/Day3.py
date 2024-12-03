import re

with open('2024/Day3/Day3Input.txt', 'r') as f:
    puzzle_input = f.read()

def solve_puzzle(puzzle_input):
    pattern = r"mul\((\-?\d+),(\-?\d+)\)"

    matches = re.findall(pattern, puzzle_input)
    part1 = 0
    for i in matches:
        part1 += (int(i[0]) * int(i[1]))

    pattern2 = r"(mul\((\-?\d+),(\-?\d+)\))|(do\(\))|(don't\(\))"
    matches2 = re.findall(pattern2, puzzle_input)

    result = []
    include = True
    for match in matches2:
        if match[0] and include:
            result.append((match[1],match[2]))
        elif match[3]:
            include = True
        elif match[4]:
            include = False
    
    part2 = 0
    for j in result:
        part2 += (int(j[0]) * int(j[1]))    



    return part1,part2

print(solve_puzzle(puzzle_input))

