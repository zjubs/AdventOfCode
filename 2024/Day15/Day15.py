

with open('2024/Day15/Day15Input.txt', 'r') as f:
    puzzle = f.read()

g,m = puzzle.split('\n\n')
g = g.split('\n')

# prep instructions
instructions = ''.join(m.split('\n'))

# prep grid
grid = {}
for i,line in enumerate(g):
    for j,chr in enumerate(line):

        if chr == '@':
            curr = (i,j)
            grid[(i,j)] = '.'
      
        else:
            grid[(i,j)] = chr

def add_tuple(tuple1,tuple2):
    return tuple(a + b for a, b in zip(tuple1, tuple2))

moves = {
    '^': (-1,0),
    '>': (0,1),
    '<': (0,-1),
    'v': (1,0)}


for dir in instructions:
    proposed = add_tuple(curr,moves[dir])
    if grid[proposed] == '.':
        curr = proposed
    elif grid[proposed] == '#':
        curr = curr
    elif grid[proposed] == 'O':     
        pos_box = proposed
        val = grid[pos_box]
        curr_boxes = []
        while val == 'O':
            curr_boxes.append(pos_box)
            pos_box = add_tuple(pos_box,moves[dir])
            val = grid[pos_box]
        
        if val == '#':
            curr = curr
        elif val == '.':
            curr = proposed
            grid[curr_boxes[0]] = '.'
            grid[pos_box] = 'O'

x = 1
part1 = 0
final_boxes = []
for key,value in grid.items():
    if value =='O':
        final_boxes.append(key)
        part1 += 100 * key[0] + key[1] 

print(part1)

x = 1












    



x = 1


