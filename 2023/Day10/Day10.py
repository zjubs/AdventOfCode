# from s iterate round whole sequence noting distance - then when retunr to S can divide by 2 to get result

#from S need to work out valid next square above 
valid_pipe = {'n': ('|', 'F','7','S'),
              'e': ('-', 'J', '7','S'),
              's': ('|','J','L','S'),
              'w': ('-','L', 'F','S')

}

moves = {
    'n': (-1,0),
    'e': (0,1),
    's': (1,0),
    'w': (0,-1)
}

opposite_move  = {
    'n': 's',
    'e': 'w',
    's': 'n',
    'w': 'e'
}


with open ('Day10\Day10Input.txt','r') as f:
    puzzle_input = f.read()

def part1(puzzle_input):

    # process grid
    lines = puzzle_input.split('\n')
    grid = {}
    start = None
    for i,line in enumerate(lines):
        for j in range(len(line)):
            grid[(i,j)] = line[j]
            if line[j] =='S':
                start = (i,j)

    # find first step
    symbol = 'S'
    exclude_move = None
    curr_position = start
    n_steps = 0 
    pipe_cells = [start]
    while not ((symbol == 'S') and (n_steps > 0)):
        # look at selection of moves
        for move in moves.keys():
                if move != exclude_move:
                    trial_position = (curr_position[0] + moves[move][0] ,curr_position[1] + moves[move][1])
                    trial_symbol = grid.get(trial_position,'?') # if not valid grid position we use ivnlaid symbol

                    # check if move is valid
                    if (trial_symbol in valid_pipe[move]) and (symbol in valid_pipe[opposite_move[move]]):
                        # move to new location
                        

                        curr_position = trial_position
                        symbol = trial_symbol
                        pipe_cells.append(curr_position)
                    
                        exclude_move = opposite_move[move]
                        n_steps += 1
                        break
    
        #print(n_steps)
        #print(curr_position)
    return (n_steps //2,pipe_cells,grid)

part1_result, pipe, grid = part1(puzzle_input)

print(part1_result)

# part 2

# clean grid up to show pipe
for cell in grid:
    if cell not in pipe:
        grid[cell] = '.'

# calc result
lines = puzzle_input.split('\n')

total_area = 0 
for i,line in enumerate(lines):
    indicator = 0 # outside line
    for j in range(len(line)):
        if grid[(i,j)] == '|':
            indicator = abs(indicator-1)
        elif grid[(i,j)] in ('F','L'):
            # find next turn
            curr = grid[(i,j)]
            while grid[(i,j)] not in ('J','7'):
                j += 1
            if (curr,grid[(i,j)]) in (('F','J'),('L','7')):
                indicator = abs(indicator-1)
        elif grid[(i,j)] == '.':
            total_area += indicator

print(total_area)

x = 1



