
with open('2024/Day16/Day16Input.txt', 'r') as f:
    puzzle = f.readlines()

from copy import deepcopy
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

#from queue import PriorityQueue
import heapq

def dijkstra(grid, start, goals):

    def get_neighbours(node):
        neighbours = []
        opposite = {
            '^': 'v',
            '>': '<',
            '<': '>',
            'v': '^'}

        directions = {
            '^': (-1,0),
            '>': (0,1),
            '<': (0,-1),
            'v': (1,0)}
        for key,value in directions.items():
            if key != opposite[node[2]]:
                nx, ny = node[0] + value[0], node[1] + value[1]
                if grid.get((nx,ny),'?') =='.':
                    neighbours.append((nx, ny,key))
        return neighbours

    open_set = []
    heapq.heappush(open_set,(0, start,[(start[0],start[1])]))  # (priority, node,path)
    g_score = {start: 0}
    valid_paths = []

    while open_set:
        score, current,path = heapq.heappop(open_set)
            
        if current in goals: # finish cond
                
            valid_paths.append((score,path))
            print(score)

        for neighbour in get_neighbours(current):
            dir_change = neighbour[2] != current[2]
            tentative_g_score = score + 1 + (int(dir_change) * 1000)

            if neighbour not in g_score or tentative_g_score <= g_score[neighbour]:
                g_score[neighbour] = tentative_g_score
                updated_path = deepcopy(path)
                updated_path.append((neighbour[0], neighbour[1]))

                heapq.heappush(open_set,(tentative_g_score, neighbour,updated_path))

    return valid_paths  # No path found

paths = dijkstra(grid, start, ends)


min_score = min([x for x,_ in paths])
print(f'part1:{min_score}')
seats = set()
for score,path in paths:
    if score == min_score:
        seats |= {*path}

print(f'part1:{len(seats)}')



#debug path
for i,line in enumerate(puzzle):
    line = line.strip() 
    curr_line = ''
    for j,chr in enumerate(line):
        
        if (i,j) in seats:
            curr_line = f'{curr_line}O'
        else:
            curr_line = f'{curr_line}{grid[i,j]}'
    print(curr_line, end='\n')





