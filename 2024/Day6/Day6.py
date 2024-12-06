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


def walk(G,part2_ind):
    pos,dir = start, G[start]
    next_shape = ''
    seen = set()
    while next_shape != '?' and (pos,dir) not in seen:
        seen |= {(pos,dir)}
        next = add_tuple(pos,dir_map[dir])
        next_shape = G.get(next,'?')
        if next_shape == '#':
            dir = dir_change[dir]
        else:
            pos = next
    if part2_ind:
        return (pos,dir) in seen
    else:
        return {pos for pos,_ in seen}

path = walk(grid, False)
part1 = print(len(path))
path.remove(start)
part2 = print(sum(walk(grid|{o:'#'},True) for o in path))