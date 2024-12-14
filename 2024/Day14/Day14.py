



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


     

