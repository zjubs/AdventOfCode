



#101,103
# sample: 11,7


import re
with open('2024/Day14/Day14Input.txt', 'r') as f:
    robots = f.read().split('\n')


pattern = r'-?\d+'

matches = re.findall(pattern, robots[0])
time = 100
#size = (11,7)
size = (101,103)
quad = {x:0 for x in range(4)}
mid = (size[0]//2,size[1]//2)
robots_final = []
for robot in robots:
    matches = re.findall(pattern, robot)
    x,y,vx,vy = (int(i) for i in matches)

    xt = x + (vx * time)
    yt = y + (vy * time)

    x2 = xt % size[0]
    y2 = yt % size[1]
    robots_final.append((x2,y2))

    if x2 < mid[0] and y2 < mid[1]:
        quad[0] +=1
    if x2 > mid[0] and y2 < mid[1]:
        quad[1] +=1
    if x2 < mid[0] and y2 > mid[1]:
        quad[2] +=1
    if x2 > mid[0] and y2 > mid[1]:
        quad[3] +=1

    zz =1

part1 = 1
for i in quad.values():
    part1 *= i
print(part1)


import matplotlib.pyplot as plt
import numpy as np

# Define grid dimensions
rows, cols = 101,103

for t in range(10000):
    robots_curr = []
    for robot in robots:
        matches = re.findall(pattern, robot)
        x,y,vx,vy = (int(i) for i in matches)

        xt = x + (vx * t)
        yt = y + (vy * t)

        x2 = xt % size[0]
        y2 = yt % size[1]
        robots_curr.append((x2,y2))

        # Create an empty grid (0 = empty, 1 = marked)
        grid = np.zeros((rows, cols), dtype=int)

    # Mark the positions
    ## these are occurences of patterns in grid so we investigate these
    if (t+1) % 103 == 66 or (t+1) % 101 == 12:
        for r, c in robots_curr:
            grid[r][c] = '1'

        # Print the grid row by row
        plt.figure(figsize=(6, 6))
        plt.imshow(grid, cmap="Greys", origin="upper")
        plt.title(f"Grid State {t+1}")
        plt.axis("off")
        plt.savefig(f"2024\Day14\pics\grid_state_{t+1}.png", dpi=300)
        plt.close()

        zz =1