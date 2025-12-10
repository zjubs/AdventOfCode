
lights_list = []
buttons_list = []
joltage_list = []
num =0
with open('2025/Day10/input.txt', 'r') as f:
    for line in f:
        z = line.split()
        #buttons[z[0]] = []
        #joltage[z[0]] = z[-1]
        lights_list.append(z[0])
        joltage_list.append(z[-1])
        buttons_list.append([])
        for i in range(len(z)-2):
            buttons_list[num].append(tuple(map(int, z[i+1].strip("()").split(","))))
        # a, b= map(int, line.split(','))
        # tiles.append((a, b))
        num+=1


def toggle(curr,button):
    #(1,0,0,1) (2,3)
    new = list(curr)
    for i in button:
        new[i] = 1 - new[i]
    return tuple(new)


result = 0
for lights,buttons in zip(lights_list,buttons_list):
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

import pulp


def toggle_jolt(curr,button):
    #(1,0,0,1) (2,3)
    new = list(curr)
    for i in button:
        new[i] +=1
    return tuple(new)

result = 0
for joltage,buttons in zip(joltage_list,buttons_list):
    targets = tuple(int(x) for x in joltage.strip("{}").split(","))
    operations = buttons
    

    
    x = 1


#     visited = {}
#     visited[tuple([0 for i in required])] = 0
#     press_count = 0
#     while required not in visited:
#         press_count +=1
#         curr_visited = list(visited.keys())
#         for pos in curr_visited:
#             for button in buttons:
#                 new_pos = toggle_jolt(pos, button)
#                 if new_pos not in visited:
#                     visited[new_pos] = press_count
        
#     result += press_count
#     print(joltage)

# print(result)

# result = 0
# for joltage,buttons in zip(joltage_list,buttons_list):
#     required = tuple(int(x) for x in joltage.strip("{}").split(","))
#     visited = {}
#     visited[tuple([0 for i in required])] = 0
#     press_count = 0
#     while required not in visited:
#         press_count +=1
#         curr_visited = list(visited.keys())
#         for pos in curr_visited:
#             for button in buttons:
#                 new_pos = toggle_jolt(pos, button)
#                 if new_pos not in visited:
#                     visited[new_pos] = press_count
        
#     result += press_count
#     print(joltage)

# print(result)


