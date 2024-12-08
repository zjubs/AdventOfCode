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



def diff_tuple(tuple1,tuple2):
    return tuple(a - b for a, b in zip(tuple1, tuple2))

def add_tuple(tuple1,tuple2):
    return tuple(a + b for a, b in zip(tuple1, tuple2))



locations = set()
part2 = 0
for key,vals in antenna.items():
    combinations = list(itertools.combinations(vals, 2))
    for i in combinations:
        diff = diff_tuple(i[0],i[1])

        if i[0] not in locations:
            locations.add(i[0])
            part2 += 1

        loc = i[0]
        while loc[0] > - 1 and loc[0] <50 and loc[1] > -1 and loc[1] <50:
            loc = add_tuple(loc, diff)
            if grid.get(loc,'?') != '?' and loc not in locations:
                locations.add(loc)
                part2 += 1

        loc = i[0]
        while loc[0] > - 1 and loc[0] <50 and loc[1] > -1 and loc[1] <50:
            loc = diff_tuple(loc,diff)
            if grid.get(loc,'?') != '?' and loc not in locations:
                locations.add(loc)
                part2 += 1


print(part2)
x = 1