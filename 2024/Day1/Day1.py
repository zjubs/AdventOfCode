

with open('2024/Day1/Day1Input.txt', 'r') as f:
    puzzle_input = f.read()


from collections import Counter

def solve_puzzle(puzzle_input):
    lines = puzzle_input.split('\n')
    left = []
    right = []
    for line in lines:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    left_sorted = sorted(left)
    right_sorted = sorted(right)

    counts = Counter(right_sorted)

    part1 = 0
    part2 = 0
    for i in range(len(left_sorted)):
        part1 += abs(left_sorted[i] - right_sorted[i])
        part2 += left_sorted[i] * counts[left_sorted[i]]


    return part1,part2,

print(solve_puzzle(puzzle_input))
