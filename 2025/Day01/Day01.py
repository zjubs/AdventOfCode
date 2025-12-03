with open('2025/Day01/input_test.txt', 'r') as f:
    puzzle_input = f.read()

dial = 50
result = result2 = 0
lines = puzzle_input.split('\n')
for i in lines:
    if i[0] == "R":

        count_zero = (dial + int(i[1:])) // 100
        new_dial = (dial + int(i[1:]) ) % 100

        
    else:
        b = abs(int(i[1:]) // 100)
        c = abs(int(i[1:])) % 100
        count_zero = b + int(c>=dial) - int(dial==0)

        new_dial = (dial - int(i[1:])) %100

    if dial == 0:
        result += 1
    
    result2 += count_zero
    dial = new_dial

print(result)
print(result2)

dial = 50
result = result2 = 0
dirs={"L": -1, "R":1}
lines = puzzle_input.split('\n')
for i in lines:
    dir, dist = dirs[i[0]], int(i[1:])
    
    new_dial = (dial + dir*dist ) % 100
    count_zero = abs((dial + dir*dist) // 100) + (1 if new_dial ==0 and dir == -1 else 0) -(1 if dial == 0 and dir == -1 else 0)


    if dial == 0:
        result += 1
    
    result2 += count_zero
    dial = new_dial

print(result)
print(result2)

