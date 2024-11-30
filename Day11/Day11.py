

with open('Day11\Day11Input.txt','r') as f:
    puzzle_input = f.read()


def part1(puzzle_input):

    # process grid
    lines = puzzle_input.split('\n')
    grid = [[ele for ele in line] for line in lines]
    m, n = len(grid), len(grid[0])
    

    i = 0
    while i < len(grid):
        if '#' not in grid[i]:
            grid.insert(i,['.'] * n)
            m += 1
            i += 2
        else: 
            i += 1
    
    print([len(x) for x in grid])
    j = 0
    while j < len(grid[0]):
        if '#' not in [grid[i][j] for i in range(m)]:
            for i in range(m):
                grid[i].insert(j,'.')
            n += 1
            j += 2
        else: 
            j += 1
    
    
    print([len(x) for x in grid])
    from itertools import combinations
    galaxies = [(x,y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == '#']
    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        total += abs(x1-x2) + abs(y1-y2)
    
    return total


print(part1(puzzle_input))

