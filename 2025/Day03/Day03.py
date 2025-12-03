
with open('2025/Day03/input.txt', 'r') as f:
    puzzle_input = f.read()

result = 0 
lines = puzzle_input.split('\n')
for line in lines:
    line_max = ''
    pos_adj = 0
    for i in range(12):
        
        if (12-i) ==1: 
            curr =  line[pos_adj:]
        else:
            curr = line[pos_adj :-(12-i-1)]

        curr_max = '0'
        
        for j,battery in enumerate(curr):
            if int(battery)> int(curr_max):
                curr_max = battery
                adj = j +1
        pos_adj += adj
        line_max = line_max + curr_max
    
    result += int(line_max)
    print(line_max)
print(result)