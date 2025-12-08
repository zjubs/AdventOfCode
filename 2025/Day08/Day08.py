
import math

junctions = []
with open('2025/Day08/input.txt', 'r') as f:
    for line in f:
        a, b, c = map(int, line.split(','))
        junctions.append((a, b, c))


# should cache this
def dist(p,q):
    return math.sqrt((p[0] - q[0])**2 +
                     (p[1] - q[1])**2 +
                     (p[2] - q[2])**2)

distances={}
for i,j1 in enumerate(junctions):
        for j,j2 in enumerate(junctions):
            if j1 != j2:
                if (j1,j2) not in distances and (j2,j1) not in distances:
                    distances[(j1,j2)] = dist(j1,j2)
x = 1

connections =  [{t} for t in junctions]
connection_count = 0

for key in sorted(distances, key=lambda k: distances[k]):
    if connection_count <1000:
        j1,j2 = key
        if not connections:
            connections.append({j1,j2})
        
        elif any(j1 in s and j2 in s for s in connections):
            # both already in same set
            pass

        elif any(j1 in s for s in connections) and not any(j2 in s for s in connections):
            for s in connections:
                if j1 in s:
                    s.add(j2)
                    break
        
        elif any(j2 in s for s in connections) and not any(j1 in s for s in connections):
            for s in connections:
                if j2 in s:
                    s.add(j1)
                    break
        
        elif any(j2 in s for s in connections) and any(j1 in s for s in connections):
            a = next(s for s in connections if j1 in s)
            b = next(s for s in connections if j2 in s)

            # merge them
            merged = a | b

            # remove the old sets
            connections.remove(a)
            connections.remove(b)

            # add the merged set
            connections.append(merged)


        elif not any(j2 in s for s in connections) and not any(j1 in s for s in connections):
            connections.append({j1,j2})

        else:
            print("condition not met")
        connection_count += 1
    

x =1
from functools import reduce
import operator
largest_lengths = sorted((len(s) for s in connections), reverse=True)[:3]
product = reduce(operator.mul, largest_lengths, 1)

print(product)


