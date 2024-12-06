

with open('2024/Day6/Day6Input.txt', 'r') as f:
    #lines = f.readlines()
    lines = f.read().split('\n')

grid = {}
for i,line in enumerate(lines):
    for j,chr in enumerate(line):
        grid[(i,j)] = chr
        if chr not in ('.','#'):
            start = (i,j)

dir_map ={
    '^': (-1,0),
    '>': (0,1),
    'v': (1,0),
    '<': (0,-1)       
}

dir_change = {
    '^':'>',
    '>':'v',
    'v':'<',
    '<':'^'
}

def add_tuple(tuple1,tuple2):
    return tuple(a + b for a, b in zip(tuple1, tuple2))



pos = start
dir = grid[start]
next_shape = ''
visited = []
while next_shape != '?':
    if pos not in visited:
            visited.append(pos)
    next = add_tuple(pos,dir_map[dir])
    next_shape = grid.get(next,'?')

    if next_shape == '#':
        dir = dir_change[dir]
    else:
        #next_shape == '.':
        pos = next



print(len(visited))


def is_loop(gridx):
    pos = start
    dir = gridx[start]
    next_shape = ''
    visitedx = set()
    while next_shape != '?':
        if (pos,dir) in visitedx:
            return True
        visitedx.add((pos,dir))
        
        next = add_tuple(pos,dir_map[dir])
        next_shape = gridx.get(next,'?')

        if next_shape == '#':
            dir = dir_change[dir]
        else:
            #next_shape == '.':
            pos = next
    return False


#search on visited only excluding start
import copy

potential = visited[1:]
part2 = 0
counter = 0
for obj in potential:
    print(counter)
    counter += 1
    grid2 = copy.deepcopy(grid)
    grid2[obj] = '#'
    if is_loop(grid2):
        print(obj)
        part2 += 1

print(part2)

x = 1




    