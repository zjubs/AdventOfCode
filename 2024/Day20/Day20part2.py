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
            return g_score[current],g_score

        for neighbour in get_neighbours(current):
            tentative_g_score = g_score[current] + 1

            if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
                g_score[neighbour] = tentative_g_score
                heappush(open_set,(tentative_g_score, neighbour))

    return None  # No path found

base,scores = dijkstra(grid, start, end)

from collections import defaultdict
cheats = defaultdict(int)

# for all source_points in scores (except last 100)
    # find all target_points within a manhatten distance of 20
        # if score of those target_points is >= 100 + source_point score +mnahatten dist
            # part2 +=1

# use sets for fast compare between target_points and manhatten points

path = set(scores.keys())

def manhattan_points(center, distance):
    x, y = center
    points = set()

    for dx in range(-distance, distance + 1):
        dy_max = distance - abs(dx)
        for dy in range(-dy_max, dy_max + 1):
            points.add((x + dx, y + dy))
    
    return points

def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1) + abs(y2 - y1)

target_cheat = 100
cheat_size = 20
part2 =0
for point in path:
    if scores[point] < (base - target_cheat):
        m_points = manhattan_points(point,cheat_size)
        target_points = m_points & path
        for p in target_points:
            if scores[p] - scores[point] - manhattan_distance(p, point) >= target_cheat:
                part2 +=1

print(part2)


x=1


