
import re

with open('2020/Day02/Day2Input.txt', 'r') as f:
    puzzle = f.read().split('\n')

def solve(puzzle: list) -> int:

    part1 = 0
    part2 = 0
    for line in puzzle:
        rule,password = line.split(': ')
        min_val, max_val = map(int,re.findall(r'\d+',rule))

        chr = rule[-1]
        counts = len(re.findall(chr, password))
        if counts >= min_val and counts <= max_val:
            part1 += 1

        if (password[min_val - 1] == chr) ^  (password[max_val -1] == chr):
            part2 +=1

    return part1,part2

p1,p2 = solve(puzzle)
print(f'Part1: {p1}')
print(f'Part2: {p2}')

