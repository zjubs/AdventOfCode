
from collections import defaultdict, deque

from heapq import heapify, heappop, heappush

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

# work out all positions we can visit and number of times (pos,score)


def bfs2(p, towels):
    visited = defaultdict(int)
    visited[0] = 1
    positions_to_check = [0]
    heapify(positions_to_check)

    while positions_to_check:
        position = heappop(positions_to_check)

        if position == len(p):
            # get combintaions and return
            # combinations += 1
            return visited[position]
        
        for key in towels:
            if key <= len(p) - position:
                for t in towels[key]:
                    if can_use_towel(p,t,position):
                        proposed_position = position + len(t)
                        visited[proposed_position] += visited[position]
                        if (position + len(t)) not in positions_to_check:
                            heappush(positions_to_check,proposed_position)

    return 0                           

part2 = 0
i =0
for pattern in patterns:
    i+=1
    print(i)
    if bfs(pattern, towels):
        part2 += bfs2(pattern, towels)

print(part2)

x = 1


