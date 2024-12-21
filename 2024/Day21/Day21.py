

from itertools import permutations
from functools import cache

@cache
def all_paths(start, end, invalid):
    """
    finds all paths between two coordinates in a grid avoiding passing through invalid coordinate
    """
    x1, y1 = start
    x2, y2 = end
    
    dx = x2 - x1  # Vertical steps
    dy = y2 - y1  # Horizontal steps

    moves = {'^': (-1,0),
             '<': (0,-1),
             '>': (0,1),
             'v': (1,0)}
    
    # Determine step directions
    u = '^' if dx < 0 else 'v'
    r = '<' if dy < 0 else '>'
    steps = [u] * abs(dx) + [r] * abs(dy)

    # Generate all unique permutations of steps
    unique_paths = set(permutations(steps))
    valid_paths = set()
    # remove any paths over invalid cell
    for path in unique_paths:
        curr_x, curr_y = x1, y1
        is_valid = True

        for move in path:
            dx,dy = moves[move]
            curr_x,curr_y = curr_x + dx, curr_y + dy

            if (curr_x, curr_y) == invalid:
                is_valid = False
                break
        
        if is_valid:
            valid_paths.add(path)

    return valid_paths

grid_numeric ={
    '7': (0,0),
    '8': (0,1),
    '9': (0,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '1': (2,0),
    '2': (2,1), 
    '3': (2,2),
    '0': (3,1), 
    'A': (3,2)  
}
grid_numeric_invalid = (3,0)

grid_direction ={
    '^': (0,1),
    'A': (0,2),
    '<': (1,0),
    'v': (1,1),
    '>': (1,2)
}
grid_direction_invalid = (0,0)

@cache
def solve_paths(paths, level,nlevels):
    """
    Count the minimum number of button presses for a code on the directional control for nlevels of robots
    This finds all paths between buttons to be pressed in the code and recurses for all required levels
    At the final recusion level required the minimum number of buttons required is calculated
    """
    curr_iter_buttonslist =[]
    for path in paths:
        path_buttons = 0
        for s1, e1, in zip(path,path[1:]):
                paths_1 = all_paths(grid_direction[s1], grid_direction[e1],grid_direction_invalid)
                if level == nlevels:
                    updated_paths_1 = {t + ('A',) for t in paths_1}
                    min_next_iter_buttons = min([len(t) for t in updated_paths_1])
                else:
                    updated_paths_1 = {('A',) + t + ('A',) for t in paths_1}
                    min_next_iter_buttons = solve_paths(frozenset(updated_paths_1), level + 1,nlevels)

                path_buttons += min_next_iter_buttons
            
        curr_iter_buttonslist.append(path_buttons)
    buttons = min(curr_iter_buttonslist) 
                
    return buttons


def process_code(code,nlevels):
    """
    Count the minimum number of button presses for a code on the numerical control for nlevels of robots
    This finds all paths between buttons to be pressed in the code
    solve_paths then returns the minimum number of button pressed for each path for the 
    number of levels of robots
    """
    buttons = 0
    # since start pointing at 'A' include move from 'A' to first element of code
    code =  'A' + code
    for s,e in zip(code, code[1:]):
        
        paths = all_paths(grid_numeric[s], grid_numeric[e],grid_numeric_invalid)
        updated_paths = {('A',) + t + ('A',) for t in paths}

        buttons += solve_paths(frozenset(updated_paths), 1,nlevels)

    return buttons

with open('2024/Day21/Day21Input.txt', 'r') as f:
    codes = f.read().split('\n')

part1 = 0
part2 = 0 
for code in codes:
    val = int(code[:3])
    part1 += val * process_code(code,2)
    part2 += val * process_code(code,25)
print(f'Part1: {part1}')
print(f'Part2: {part2}')
