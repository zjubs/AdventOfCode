
with open('2024/Day9/Day9Input.txt', 'r') as f:
    puzzle = f.read()


blocks = []
num = 0 
for i,file in enumerate(puzzle):
    if  i % 2:
        for j in range(int(file)):
            blocks.append(-1)
    else:
        for j in range(int(file)):
            blocks.append(num)
        num += 1


#move files
while -1 in blocks:
    if blocks[-1] == (-1):
        blocks.pop()
    else:
        index = blocks.index(-1)
        blocks[index] = blocks.pop()

#calc checksum
part1 = 0
for i,x in enumerate(blocks):
    part1 += i * x

print(part1)
    
