
from operator import add,mul

def cat(x,y):
    return int(str(x) + str(y))

ops = [add, mul]
ops2 = (add, mul,cat)

part1 = 0
part2 = 0
with open('2024/Day7/Day7Input.txt', 'r') as f:
    lines = f.read().split('\n')

for line in lines:
    test_val,inputs = line.split(': ')
    test_val = int(test_val)
    inputs = [int(x) for x in inputs.split()]
    
    S = [inputs[0]]
    S2 = [inputs[0]]
    for input in inputs[1:]:
        #S = [op(s,input) for s in S for op in ops]
        S2 = [op(s,input) for s in S2 for op in ops2]
    if test_val in S:
        part1 += test_val
    if test_val in S2:
        part2 += test_val

print(part1)
print(part2)

x = 1










part1 = 0
for l in open('2024/Day7/Day7Input.txt', 'r'):
    x = l.split()
    x[0] = x[0][:-1]
    test_val,*inputs=map(int,x)

    S = [inputs[0]]
    for input in inputs[1:]:
        S = [op(s,input) for s in S for op in ops]
        if test_val in S:
            part1 += test_val
print(part1)
z =1
