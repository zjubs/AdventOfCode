import matplotlib.pyplot as plt
from functools import lru_cache

tiles = []
with open('2025/Day09/input.txt', 'r') as f:
    for line in f:
        a, b= map(int, line.split(','))
        tiles.append((a, b))

def area(p,q):
    return (abs(p[0] - q[0])+1) * (abs(p[1] - q[1])+1)

areas={}
for i,j1 in enumerate(tiles):
        for j,j2 in enumerate(tiles):
            if j1 != j2:
                areas[(j1,j2)] = area(j1,j2)

x =1 

print(max(areas.values()))

def plot_path(points):

    # unpack into separate x and y lists
    xs, ys = zip(*points)

    plt.figure(figsize=(10, 10))

    plt.plot(xs, ys, marker='.', linewidth=1) 
    plt.scatter(xs, ys, s=5) 

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    plt.show()

#plot_path(tiles)
#50126
#51075

# find all valid ranges in each row
valid_by_row = {}
for i,tile in enumerate(tiles):
    t1 = tile
    t2 = tiles[(i + 1) % len(tiles)]

    x1,y1 = t1
    x2,y2 = t2

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if y not in valid_by_row:
                valid_by_row[y] = (x1,x1)
            else:
                valid_by_row[y] = (min(x1,valid_by_row[y][0]),max(x1,valid_by_row[y][1]))
    if y1 == y2:
        if y1 not in valid_by_row:
            valid_by_row[y1] = (min(x1,x2), max(x1,x2))
        else:
            valid_by_row[y1] = (min(valid_by_row[y1][0],x1,x2),max(valid_by_row[y1][1],x1,x2))

def test_valid(tile1,tile2):
    # find if rectangle is valid
    min_y = min(tile1[1],tile2[1])
    max_y = max(tile1[1],tile2[1])
    min_x = min(tile1[0],tile2[0])
    max_x = max(tile1[0],tile2[0])

    for y in range(min_y,max_y +1):
        if y not in valid_by_row:
            return False
        if min_x < valid_by_row[y][0] or max_x  > valid_by_row[y][1]:
            return False
    return True



# find all valid points in each row
areas2={}
for i,j1 in enumerate(tiles):
        for j,j2 in enumerate(tiles):
            #print(f"({i},{j})")           
            if j1 != j2:
                if test_valid(j1,j2):
                    areas2[(j1,j2)] = area(j1,j2)

    
print(max(areas2.values()))