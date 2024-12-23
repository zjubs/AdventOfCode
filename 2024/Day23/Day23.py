
from collections import defaultdict

with open('2024/Day23/Day23Input.txt', 'r') as f:
    edges = f.read().split('\n')

nodes = defaultdict(list)
for edge in edges:
    a,b  = edge.split('-')
    nodes[a].append(b)
    nodes[b].append(a)


t_nodes = [x for x in nodes if x[0] == 't']

combinations = set()
for t_node in t_nodes:
    for i in nodes[t_node]:
        for j in nodes[i]:
            if t_node in nodes[j]:
                combinations.add(tuple(sorted((t_node,i,j))))


print(f'Part1: {len(combinations)}')




x=1 