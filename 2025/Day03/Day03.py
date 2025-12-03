
with open('2025/Day03/input.txt', 'r') as f:
    puzzle_input = f.read()


lines = puzzle_input.split('\n')
n_batteries = [2,12] #part1,part2
for n in n_batteries:
    result = 0 
    for line in lines:
        line_max = ''
        start = 0

        for i in range(n,0,-1):
            
            if i == 1:
                curr =  line[start:]
            else:
                curr = line[start:-(i-1)]

            curr_max = '0'
            
            for j,battery in enumerate(curr):
                if int(battery)> int(curr_max):
                    curr_max = battery
                    start_adj = j + 1
            start += start_adj
            line_max = line_max + curr_max
        
        result += int(line_max)

    print(result)