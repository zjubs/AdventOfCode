

from itertools import permutations
from functools import cache

@cache
def all_paths(start, end,invalid):
    # invalid should be the ref for the empty cell in the ocntrol panel being used

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

print(all_paths((0,0),(2,2),(0,1)))

print(all_paths((1,1),(4,1),(0,1)))


grid_numeric_rev ={
    (0,0): '7',
    (0,1): '8',
    (0,2): '9',
    (1,0): '4',
    (1,1): '5',
    (1,2): '6',
    (2,0): '1',
    (2,1): '2', 
    (2,2): '3',
    (3,1): '0', 
    (3,2): 'A',  
}
grid_numeric = {val: key for key,val in grid_numeric_rev.items()}
grid_numeric_invalid = (3,0)

grid_direction_rev ={
    (0,1): '^',
    (0,2): 'A',
    (1,0): '<',
    (1,1): 'v',
    (1,2): '>'
}
grid_direction_invalid = (0,0)
grid_direction  = {val: key for key,val in grid_direction_rev.items()}

# remember to start at A
code =  'A' + '029A'

def process_code(code):
    buttons = 0 
    for s,e in zip(code, code[1:]):
        buttons_this_step = 100
        paths = all_paths(grid_numeric[s], grid_numeric[e],grid_numeric_invalid)
        updated_paths = {('A',) + t + ('A',) for t in paths}

        level1buttonslist =[]
        for path in updated_paths:
            level1_buttons = 0
            for s1, e1, in zip(path,path[1:]):
                    paths_1 = all_paths(grid_direction[s1], grid_direction[e1],grid_direction_invalid)
                    updated_paths_1 = {('A',) + t + ('A',) for t in paths_1}

                    
                    level2buttonslist =[]
                    for path_1 in updated_paths_1:
                        level2_buttons = 0
                        for s2, e2, in zip(path_1,path_1[1:]):
                                paths_2 = all_paths(grid_direction[s2], grid_direction[e2],grid_direction_invalid)
                                updated_paths_2 = {t + ('A',) for t in paths_2}
                                min_buttons = min([len(t) for t in updated_paths_2])

                                level2_buttons += min_buttons
                        level2buttonslist.append(level2_buttons)

                    min_level1_buttons = min(level2buttonslist)
                    level1_buttons += min_level1_buttons
            level1buttonslist.append(level1_buttons)
        buttons += min(level1buttonslist)
    return buttons

print(process_code(code))

x = 1                    


with open('2024/Day21/Day21Input.txt', 'r') as f:
    codes = f.read().split('\n')
part1 = 0 
for code in codes:
    val = int(code[:3])
    code =  'A' + code
    part1 += val * process_code(code)
print(part1)
x = 1

#find min for each path
# sum for each s2,e2
# find min for each path 1






#'029A77'
# directions
# diresctions
# directions

# find all combinations at lowest level
# then find all combinations at next level
# find all combinations at last level

# robots start pointing at A

# need shortest sequence, but that means findshortest at each level then find shortest way of doing that above.