
from collections import defaultdict, deque

# process inputs
with open('2024/Day19/Day19Input.txt', 'r') as f:
    towels_in,patterns = f.read().split('\n\n')


patterns = patterns.split('\n')
towels = defaultdict(list)

for towel in towels_in.split(', '):
    towels[len(towel)].append(towel)


def can_use_towel(p,t,position):
    return p[position:(position + len(t))] == t

def bfs(p, towels):
    visited = set()
    queue = deque([0])

    while queue:
        position = queue.popleft()

        if position == len(p):
            return True
        

        if position not in visited:
            visited.add(position)

            for key in towels:
                if key <= len(p) - position:
                    for t in towels[key]:
                        if can_use_towel(p,t,position):
                            if (position + len(t)) not in visited:
                                queue.append(position + len(t))

    return False                            

                


x = 1
part1 = 0
for pattern in patterns:
    if bfs(pattern, towels):
        part1 +=1

print(part1)

x=1

