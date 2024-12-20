from heapq import heapify, heappush,heappop

with open('2024/Day20/Day20Input.txt', 'r') as f:
    puzzle = f.read().split('\n')

rows = len(puzzle)
cols = len(puzzle[0])

grid = {}
walls = []
for i,line in enumerate(puzzle):
    for j,chr in enumerate(line):

        grid[(i,j)] = chr

        if chr == '#':
            walls.append((i,j))        
                
        if chr == 'E':            
            end = (i,j)
            grid[(i,j)] = '.'

        if chr == 'S':
            start = (i,j)
            grid[(i,j)] = '.'


def dijkstra(grid, start, goal):

    def get_neighbours(node):
        neighbours = []
        directions = [
            (-1,0),
            (0,1),
            (0,-1),
            (1,0)]
        for value in directions:
            nx, ny = node[0] + value[0], node[1] + value[1]
            if grid.get((nx,ny),'?') =='.':
                neighbours.append((nx, ny))
        return neighbours

    open_set = []
    heapify(open_set)
    heappush(open_set,(0, start))  # (priority, node)
    g_score = {start: 0}

    while open_set:
        score, current = heappop(open_set)

        if current == goal:
            return g_score[current]

        for neighbour in get_neighbours(current):
            tentative_g_score = g_score[current] + 1

            if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
                g_score[neighbour] = tentative_g_score
                heappush(open_set,(tentative_g_score, neighbour))

    return None  # No path found

base = dijkstra(grid, start, end)

from collections import defaultdict
cheats = defaultdict(int)
part1 = 0 

walls = [(i,j) for (i,j) in walls if i != 0 and j != 0 and i != 140 and j != 140]

for i,wall in enumerate(walls):
    print(i)
    grid[wall] = '.'
    time = dijkstra(grid,start,end)
    grid[wall] = '#'
    if time < base:
        cheats[(base-time)] +=1
    if base - time >= 100:
        part1+= 1

print(part1)
    



x = 1