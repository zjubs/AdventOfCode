


with open('2024/Day4/Day4Input.txt', 'r') as f:
    lines = f.readlines()

grid = {}
for i,line in enumerate(lines):
    for j,chr in enumerate(line):
        grid[(i,j)] = chr

x = 1

dir_map ={
    'n': [(0,0),(-1,0),(-2,0),(-3,0)],
    'ne': [(0,0),(-1,1),(-2,2),(-3,3)],
    'e': [(0,0),(0,1),(0,2),(0,3)],
    'se': [(0,0),(1,1),(2,2),(3,3)],
    's': [(0,0),(1,0),(2,0),(3,0)],
    'sw': [(0,0),(1,-1),(2,-2),(3,-3)],
    'w': [(0,0),(0,-1),(0,-2),(0,-3)],
    'nw': [(0,0),(-1,-1),(-2,-2),(-3,-3)]          
}
word = 'XMAS'


def add_tuple(tuple1,tuple2):
    return tuple(a + b for a, b in zip(tuple1, tuple2))

part1 = 0
for pos,chr in grid.items():
    for dir in dir_map:
        letters = [grid.get(add_tuple(pos,coord),'?') for coord in dir_map[dir]]
        curr_word = ''.join(str(x) for x in letters)
        if curr_word == word:
            part1 += 1

print(part1)

dir_map ={
    #'n': [(0,0),(-1,0),(-2,0)],
    'ne': [(0,0),(-1,1),(-2,2)],
    #'e': [(0,0),(0,1),(0,2)],
    'se': [(0,0),(1,1),(2,2)],
    #'s': [(0,0),(1,0),(2,0)],
    'sw': [(0,0),(1,-1),(2,-2)],
    #'w': [(0,0),(0,-1),(0,-2)],
    'nw': [(0,0),(-1,-1),(-2,-2)]          
}

centres = []    
word = 'MAS'
for pos,chr in grid.items():
    for dir in dir_map:
        letters = [grid.get(add_tuple(pos,coord),'?') for coord in dir_map[dir]]
        curr_word = ''.join(str(x) for x in letters)
        if curr_word == word:
            centres.append(add_tuple(pos,dir_map[dir][1]))


from collections import Counter

counts = Counter(centres)
part2 = 0
for x in counts.values():
    if x ==2:
        part2 += 1

print(part2)
x = 1
