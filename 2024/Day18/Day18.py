import heapq


with open('2024/Day18/Day18Input.txt', 'r') as f:
    puzzle = f.read().split('\n')

coords = []
for line in puzzle:
    line = line.split(',')
    coords.append((int(line[0]),int(line[1])))
x = 1
#res = [(int(x[0]),int(x[1])) for x.split(',') in puzzle]

x = 1

#sample inputs
# grid_size = (7,7)
# initial_num_coords = 12
# valid_coords = coords[:12]
# start = (0,0)
# end = (6,6)

#actual inputs
grid_size = (71,71)
initial_num_coords = 1024
valid_coords = coords[:initial_num_coords]
start = (0,0)
end = (70,70)



# prep grid
grid = {}
for i in range(grid_size[0]):
    for j in range (grid_size[1]):
        grid[(i,j)] = '.'

for c in valid_coords:
    grid[c] = '#'


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
    heapq.heappush(open_set,(0, start))  # (priority, node)
    g_score = {start: 0}

    while open_set:
        score, current = heapq.heappop(open_set)

        if current == goal:
            return g_score[current]

        for neighbour in get_neighbours(current):
            tentative_g_score = g_score[current] + 1

            if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
                g_score[neighbour] = tentative_g_score
                heapq.heappush(open_set,(tentative_g_score, neighbour))

    return None  # No path found

path = dijkstra(grid, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found.")


#debug path
def print_grid():
    for i in range(grid_size[0]):
        curr_line=''
        for j in range(grid_size[1]):

            curr_line = f'{curr_line}{grid[(i,j)]}'
        print(curr_line, end='\n')


for coord in coords[initial_num_coords:]:
    grid[coord] = '#'
    path = dijkstra(grid, start, end)
    if path is None:
        print(f'part2: {coord}')
        break



