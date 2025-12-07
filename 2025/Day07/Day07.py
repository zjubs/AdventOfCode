
with open('2025/Day07/input.txt', 'r') as f:
    puzzle = f.read().split('\n')


result = 0 
beams = set()
for i,line in enumerate(puzzle):
    add_beams=set()
    remove_beams=set()
    for j,chr in enumerate(line):
        if chr =="S":
            add_beams.add(j)
        if chr == "^" and (j in beams):
            add_beams.add(j-1)
            add_beams.add(j+1)
            remove_beams.add(j)
            result += 1

    beams = beams - remove_beams
    beams = beams.union(add_beams)

print(result)

#if ^ split

grid = {}

result = 0 
beams = set()
for i,line in enumerate(puzzle):
    add_beams=set()
    remove_beams=set()
    for j,chr in enumerate(line):
        if chr =="S":
            add_beams.add(j)
            grid[(i,j)] = 1
            
        if chr == "^" and (j in beams):
            add_beams.add(j-1)
            add_beams.add(j+1)
            remove_beams.add(j)
            result += 1
            grid[(i,j-1)] = grid.get((i,j-1), 0) + grid[(i-1,j)]
            grid[(i,j+1)] = grid.get((i,j+1), 0) + grid[(i-1,j)]
        if chr == "." and grid.get((i-1,j)):
            # if beam above dot
            grid[(i,j)] = grid.get((i,j), 0) + grid[(i-1,j)]

    beams = beams - remove_beams
    beams = beams.union(add_beams)

print(result)

result2 = sum(v for (i, j), v in grid.items() if i == (len(puzzle)-1))
print(result2)