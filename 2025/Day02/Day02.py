with open('2025/Day02/input.txt', 'r') as f:
    puzzle_input = f.read()


ranges = puzzle_input.split(',')
result = 0
for r in ranges:
    start,end = r.split('-')
    for num in range(int(start), int(end)+1):
        x = str(num)
        l = int(len(x)/2)
        x1= x[:l]
        x2 =x[l:]

        if x1 == x2:
            result +=int(x)



print(result)


result2 = 0
for r in ranges:
    start,end = r.split('-')
    for num in range(int(start), int(end)+1):
        x = str(num)

        for l in range(1,int(len(x)/2)+1):
        
            x1= x[:l]
            
            if len(x) % l == 0:
                if x == (x1 * int(len(x)/l)):
                    result2 +=int(x)
                    break
            



print(result2)
