
with open('2024/Day2/Day2Input.txt', 'r') as f:
    puzzle_input = f.read()


def solve_puzzle(puzzle_input):
    lines = puzzle_input.split('\n')
    part1 = 0
    part2 = 0 
    for line in lines:
        levels = line.split()
        diffs = [int(levels[i]) - int(levels[i-1]) for i in range(1,len(levels)) ]
        all_postive = all([diff > 0 for diff in diffs])
        all_negative = all([diff < 0 for diff in diffs])
        all_inrange = all([abs(diff) < 4 for diff in diffs])

        if (all_postive or all_negative) and all_inrange:
            part1 += 1
            part2 += 1
        
        else:
        
            for  i in range(len(line)):
                levels_n = levels[:i] + levels[i + 1:]
                diffs = [int(levels_n[i]) - int(levels_n[i-1]) for i in range(1,len(levels_n)) ]
                all_postive = all([diff > 0 for diff in diffs])
                all_negative = all([diff < 0 for diff in diffs])
                all_inrange = all([abs(diff) < 4 for diff in diffs])

                if all_postive or all_negative:
                    if all_inrange:
                        part2 += 1
                        break
     
    
    return part1, part2


print(solve_puzzle(puzzle_input))