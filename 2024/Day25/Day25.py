
from collections import defaultdict
with open('2024/Day25/Day25Input.txt', 'r') as f:
    keys_locks = f.read().split('\n\n')

locks =[]
keys = []

for item in keys_locks:
    counts = defaultdict(int)
    rows = item.split('\n')
    
    for row in rows:
        for i,val in enumerate(row):
            if val == '#':
                counts[i] += 1

    if all([x == '#' for x in rows[0]]):
        locks.append(counts)
    else:
        keys.append(counts)

part1 =0
for key in keys:
    for lock in locks:
        valid = all([((key[pos] + lock[pos]) <=7) for pos in key.keys()])
        if valid:
            part1 += 1

print(part1)


