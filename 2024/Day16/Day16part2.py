
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

#from queue import PriorityQueue
import heapq

def dijkstra(grid, start, goals):
    """
    grid: 2D list where 0 represents a free cell and 1 represents an obstacle.
    start: Tuple (x, y) representing the start position.
    goal: Tuple (x, y) representing the goal position.
    """
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

    #open_set = PriorityQueue()
    open_set = []
    heapq.heappush(open_set,(0, start))  # (priority, node)
    came_from = {}  # To reconstruct the path later
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current in goals:
            # Reconstruct the path
            # this is nonesense
            #nodes_to_check = PriorityQueue()
            nodes_to_check = []
            heapq.heappush(nodes_to_check,current)
            visited = {start}
            path = {(start[0],start[1])}
            while nodes_to_check:
                x = heapq.heappop(nodes_to_check)
                path.add((x[0],x[1]))
                visited.add(x)
                for node in came_from.get(x,None):
                    if node not in visited:
                        heapq.heappush(nodes_to_check,node)
                    
            print(g_score[current])
            return path 

        for neighbour in get_neighbours(current):
            dir_change = neighbour[2] != current[2]
            tentative_g_score = g_score[current] + 1 + (int(dir_change) * 1000)

            if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
                #came_from[neighbour] = came_from.get(neighbour,[]).append(current)
                came_from.setdefault(neighbour, []).append(current)
                g_score[neighbour] = tentative_g_score
                heapq.heappush(open_set,(tentative_g_score, neighbour))

    return None  # No path found

path = dijkstra(grid, start, ends)
if path:
    print("Path found:", path)
else:
    print("No path found.")


#debug path
for i,line in enumerate(puzzle):
    line = line.strip() 
    curr_line = ''
    for j,chr in enumerate(line):
        
        if (i,j) in path:
            curr_line = f'{curr_line}O'
        else:
            curr_line = f'{curr_line}{grid[i,j]}'
    print(curr_line, end='\n')

x = 1



