
#from helper.helper import aoc_timer

with open('2020/Day01/Day1Input.txt', 'r') as f:
    entries = {*map(int,f.read().split('\n'))}

def part1(entries: set,target: int) -> int | None:
    for x in entries:
        y = target - x
        if  y in entries:
            return x * y
    return None


def part2(entries: set,target: int) -> int | None:
    for z in entries:
        if (xy :=part1(entries,target - z)):
            return xy * z
    return None

print(f'Part1: {part1(entries,2020)}')
print(f'Part2: {part2(entries,2020)}')



