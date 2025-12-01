with open('2025/Day01/input.txt', 'r') as f:
    puzzle_input = f.read()

start = 50
curr = start
result = 0
result2 =0
lines = puzzle_input.split('\n')
for i in lines:
    if i[0] == "R":

        a = (curr + int(i[1:])) // 100
        new_curr = (curr + int(i[1:]) ) % 100

        
    else:
        b = abs(int(i[1:]) // 100)
        c = abs(int(i[1:])) % 100
        a = b + int(c>=curr) - int(curr==0)

        new_curr = (curr - int(i[1:])) %100

        

    if curr == 0:
        result += 1
    
    
    result2 += a
    curr = new_curr

print(result)
print(result2)