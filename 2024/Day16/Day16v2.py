
with open('2024/Day16/Day16Sample.txt', 'r') as f:
    puzzle = f.readlines()

# prep grid
grid = {}
for i,line in enumerate(puzzle):
    for j,chr in enumerate(line):

        if chr == 'E':            
            grid[(i,j)] = '.'
            ends = [(i,j,x) for x in ('>','<','^','v')]
        elif chr == 'S':
            grid[(i,j)] = '.'
            start = (i,j,'>')
        else:
            grid[(i,j)] = chr

from queue import PriorityQueue

def dijkstra(grid, start, goals):

    def get_neighbours(node):
        neighbours = []
        directions = {
            '^': (-1,0),
            '>': (0,1),
            '<': (0,-1),
            'v': (1,0)}
        for key,value in directions.items():
            nx, ny = node[0] + value[0], node[1] + value[1]
            if grid.get((nx,ny),'?') =='.':
                neighbours.append((nx, ny,key))
        return neighbours

    open_set = PriorityQueue()
    open_set.put((0, start))  # (priority, node)
    g_score = {start: 0}

    while not open_set.empty():
        _, current = open_set.get()

        if current in goals:
            return g_score[current]

        for neighbour in get_neighbours(current):
            dir_change = neighbour[2] != current[2]
            tentative_g_score = g_score[current] + 1 + (int(dir_change) * 1000)

            if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
                g_score[neighbour] = tentative_g_score
                open_set.put((tentative_g_score, neighbour))

    return None  # No path found

path = dijkstra(grid, start, ends)
if path:
    print("Path found:", path)
else:
    print("No path found.")
