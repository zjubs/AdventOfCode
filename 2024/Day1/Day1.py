

with open('2024/Day1/Day1Input.txt', 'r') as f:
    puzzle_input = f.read()


def part1(puzzzle_input):
    lines = puzzle_input.split('\n')
    left = []
    right = []
    for line in lines:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    left_sorted = sorted(left)
    right_sorted = sorted(right)

    result = [abs(a - b) for a, b in zip(left_sorted, right_sorted)]
    x = 1


    return sum(result)

print(part1(puzzle_input))


def part2(puzzle_input):
    lines = puzzle_input.split('\n')
    left_dict = {}
    left_count= {}
    left= []
    right = []
    for line in lines:
        a, b = line.split()
        left_dict[int(a)] = 0
        left_count[int(a)] = 0
        right.append(int(b))
        left.append(int(a))
    
    keys = left_dict.keys()
    for i in range(len(right)):
        if right[i] in keys:
            left_dict[right[i]] += 1
        if left[i] in keys:
            left_count[left[i]] += 1

    result = 0        

    for key,val in left_dict.items():
        result += key * val * left_count[key]
    x = 1


    return result

print(part2(puzzle_input))
    
