

from math import lcm

with open('Day8/Day8Input.txt','r') as f:
    puzzle_input  = f.read()


def part1(puzzle_input):
    lines = puzzle_input.split('\n')

    instructions = lines[0]

    node_map = {}
    for line in lines[2:]:
        key, value = line.split(' = ')

        value_tuple = tuple(value.strip("()").split(", "))
        node_map[key] = value_tuple

    curr_node = 'AAA'
    n = len(instructions)
    iter = 0

    dir_map = {'L': 0, 'R':1}

    while curr_node != 'ZZZ':
        i_num = iter % n
        direction = instructions[i_num]
        options = node_map[curr_node]
        curr_node = options[dir_map[direction]]

        iter += 1

    return iter


print(part1(puzzle_input))

def part2(puzzle_input):
    lines = puzzle_input.split('\n')

    instructions = lines[0]

    node_map = {}
    for line in lines[2:]:
        key, value = line.split(' = ')

        value_tuple = tuple(value.strip("()").split(", "))
        node_map[key] = value_tuple

    
    n = len(instructions)
    
    dir_map = {'L': 0, 'R':1}

    start_nodes = [node for node in node_map.keys() if node.endswith('A')]
    print(len(start_nodes ))

    def run_node(curr_node):
        print('start')

        iter = 0
        while  not curr_node.endswith('Z'):
            i_num = iter % n
            direction = instructions[i_num]
            options = node_map[curr_node]
            curr_node = options[dir_map[direction]]

            iter += 1

        return iter
    
    node_cycle = [run_node(node) for node in start_nodes]

    lcm(*node_cycle)

    return(lcm(*node_cycle))

print(part2(puzzle_input))