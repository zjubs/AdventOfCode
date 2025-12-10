
lights_dict = {}
buttons = {}
joltage = {}
num =0
with open('2025/Day10/input.txt', 'r') as f:
    for line in f:
        z = line.split()
        buttons[z[0]] = []
        joltage[z[0]] = z[-1]
        for i in range(len(z)-2):
            buttons[z[0]].append(tuple(map(int, z[i+1].strip("()").split(","))))
        # a, b= map(int, line.split(','))
        # tiles.append((a, b))


def toggle(curr,button):
    #(1,0,0,1) (2,3)
    new = list(curr)
    for i in button:
        new[i] = 1 - new[i]
    return tuple(new)


result = 0
for lights,buttons in buttons.items():
    required = tuple([1 if c == '#' else 0 for c in lights.strip("[]")])
    visited = {}
    visited[tuple([0 for i in required])] = 0
    press_count = 0
    while required not in visited:
        press_count +=1
        curr_visited = list(visited.keys())
        for pos in curr_visited:
            for button in buttons:
                new_pos = toggle(pos, button)
                if new_pos not in visited:
                    visited[new_pos] = press_count
        
    result += press_count

print(result)


