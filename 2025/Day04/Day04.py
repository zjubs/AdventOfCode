import itertools

with open('2025/Day04/input.txt', 'r') as f:
    lines = f.read().split('\n')


grid = {}
for i,line in enumerate(lines):
    for j,chr in enumerate(line):
        grid[(i,j)] = chr



def add_tuple(tuple1,tuple2):
    return tuple(a + b for a, b in zip(tuple1, tuple2))

def count_neighbours(curr_loc):
    vals=[-1,0,1]
    tuples=[t for t in itertools.product(vals,repeat=2) if t!=(0,0)]
    count_roll = 0
    neighbours = []
    for t in tuples:
        next = add_tuple(curr_loc,t)
        if grid.get(next,".") == "@":
            count_roll +=1

    return count_roll

# part 1
result = 0 
for k,v in grid.items():
    if v == "@":
        if count_neighbours(k) < 4:
            result +=1

print(result)


# part 2
result2 =0
while True:
    total = 0
    for k,v in grid.items():
        if v == "@":
            if count_neighbours(k) < 4:
                grid[k] = '.'
                total += 1
    result2 += total
    print(f"total:{total}")
    if total == 0:
        break
print(result2)



