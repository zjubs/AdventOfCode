
import itertools

with open('2024/Day8/Day8Input.txt', 'r') as f:
    lines = f.read().split('\n')

grid = {}
antenna = {}
for i,line in enumerate(lines):
    for j,chr in enumerate(line):
        grid[(i,j)] = chr
        if chr not in ('.'):
            curr = antenna.get(chr,[])
            curr.append((i,j))
            antenna[chr] = curr

x = 1

def diff_tuple(tuple1,tuple2):
    return tuple(a - b for a, b in zip(tuple1, tuple2))

def add_tuple(tuple1,tuple2):
    return tuple(a + b for a, b in zip(tuple1, tuple2))

locations = set()
part1 = 0
for key,vals in antenna.items():
    combinations = list(itertools.combinations(vals, 2))
    for i in combinations:
        diff = diff_tuple(i[0],i[1])
        for loc in add_tuple(i[0],diff), diff_tuple(i[1],diff):
            if grid.get(loc,'?') != '?' and loc not in locations:
                locations.add(loc)
                part1 += 1

print(part1)

