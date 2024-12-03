import re

with open('2024/Day3/Day3Input.txt', 'r') as f:
    puzzle_input = f.read()

def solve_puzzle(puzzle_input):

    pattern = r"mul\((\-?\d+),(\-?\d+)\)|(do\(\))|(don't\(\))"
    matches = re.findall(pattern, puzzle_input)
    part1 = 0
    part2 = 0
    include = True
    for a,b,do,dont in matches:
        if do or dont:
            include = bool(do)
        else:
            part2 += int(a) * int(b) * include
            part1 += int(a) * int(b)



    return part1,part2

print(solve_puzzle(puzzle_input))
