
with open('Day9/Day9Input.txt','r') as f:
    puzzle_input = f.read()



def calc_diffs(x):
    return [x[i]- x[i-1] for i in range(1,len(x))]

def extrapolate_history(history):

    iter_diffs = history
    diffs = {0: history}
    iteration = 0 

    while not all(diff == 0 for diff in iter_diffs):
        iter_diffs = calc_diffs(iter_diffs)
        iteration += 1
        diffs[iteration] = iter_diffs
    
    while iteration != 0:

        # get last element of diff
        next_iteration_last_element = diffs[iteration -1][-1]
        this_iteration_last_element = diffs[iteration][-1]
        diffs[iteration -1].append(next_iteration_last_element + this_iteration_last_element)

        iteration -= 1
    
    return diffs[0][-1]

def part1(puzzle_input):
    lines = puzzle_input.split('\n')

    res = 0
    for line in lines:
        history = [int(x) for x in line.split()]
        res += extrapolate_history(history)
    return res

print(part1(puzzle_input))

def part2(puzzle_input):
    lines = puzzle_input.split('\n')

    res = 0
    for line in lines:
        history = [int(x) for x in line.split()]
        res += extrapolate_history(history[::-1]) # just reverse list from part1
    return res

print(part2(puzzle_input))