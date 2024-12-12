
with open('2024/Day12/Day12Input.txt', 'r') as f:
    lines = f.read().split('\n')

grid = {}
for i,line in enumerate(lines):
    for j,chr in enumerate(line):
            grid[(i,j)] = chr

def add_tuple(tuple1,tuple2):
    return tuple(a + b for a, b in zip(tuple1, tuple2))

moves = ((0,1),(1,0),(-1,0),(0,-1))

to_explore = set(grid.keys())

part1 = 0
while to_explore:
    next_pos = to_explore.pop()
    curr_plant = grid[next_pos]

    region_to_explore = {next_pos}
    region_explored= set()

    region_area = 0
    region_border = 0

    while(region_to_explore):
        curr_pos = region_to_explore.pop()
        region_area +=1
        region_border += 4
        region_explored.add(curr_pos)
        for move in moves:
            new_pos = add_tuple(curr_pos,move)
            if grid.get(new_pos,'') == curr_plant:
                region_border -=1
                if new_pos not in region_explored:
                    region_to_explore.add(new_pos)
    
    to_explore = to_explore - region_explored
            
    
    part1 += (region_area * region_border)

print(part1)


          