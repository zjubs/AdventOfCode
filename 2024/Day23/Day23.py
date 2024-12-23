from collections import defaultdict

with open('2024/Day23/Day23Input.txt', 'r') as f:
    edges = f.read().split('\n')

nodes = defaultdict(set)
for edge in edges:
    a,b  = edge.split('-')
    nodes[a].add(b)
    nodes[b].add(a)


combinations = []
combinations_seen = set()
combinations_t = []
for node in nodes:
    for i in nodes[node]:
        for j in nodes[i]:
            if node in nodes[j]:
                curr_set = set((node,i,j)) 
                if curr_set not in combinations_seen:
                    combinations_seen.add(frozenset(curr_set))
                    combinations.append(curr_set)
                    if 't' in (node[0],i[0],j[0]):
                        combinations_t.append(curr_set)

print(f'Part1: {len(combinations_t)}')


for node in nodes:
    for combination in combinations:
        if combination.issubset(nodes[node]):
            combination.add(node)

largest = sorted(combinations, key = lambda s: len(s))[-1]
print(f'Part2: {','.join(sorted(list(largest)))}')