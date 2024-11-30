import re

with open('Day6/Day6Input.txt', 'r') as f:
    puzzle_input = f.read()


print(puzzle_input)

times, distances = puzzle_input.split('\n')
times = map(int, re.findall('\d+', times))
distances = map(int, re.findall('\d+', distances))


total = 1
for t,d in zip(times,distances):
    wins = 0
    for speed in range(1,t):
        travel = speed * (t - speed)
        if travel > d:
            wins += 1
    print(wins)
    total *= wins

print(total)

# part 2

time, distance = puzzle_input.split('\n')
time = int(''.join(re.findall('\d+', time)))
distance = int(''.join(re.findall('\d+', distance)))



import math
exact = (time - math.sqrt(time**2 - 4 * distance))/2




print(exact * (time-exact))
# result part 2
print(time - (int(exact+1) * 2)  + 1)

x = 1