

import re
with open('2024/Day14/Day14Input.txt', 'r') as f:
    robots = f.read().split('\n')


pattern = r'-?\d+'

matches = re.findall(pattern, robots[0])
time = 100
#size = (11,7)
size = (101,103)

mid = (size[0]//2,size[1]//2)


def calc_safety_factor(time):
    robots_final = []
    quad = {x:0 for x in range(4)}
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

    safety_factor = 1
    for i in quad.values():
        safety_factor *= i
    return safety_factor


min_factor = calc_safety_factor(100)
part2 = 0
times = [x for x in range(1,10000,1)]
scores = []
for t in range(1,10000,1):
    curr_factor = calc_safety_factor(t)
    scores.append(curr_factor)
    if curr_factor < min_factor:
        part2 = t
        min_factor = curr_factor
        

print(part2)

# view the saftey scores
import matplotlib.pyplot as plt

x = times
y = scores

# Create a scatter plot
plt.scatter(x, y, s=1)
plt.xlabel("time")
plt.ylabel("safety factor")
plt.title("Scatter Plot of time vs safety score")

plt.show()


