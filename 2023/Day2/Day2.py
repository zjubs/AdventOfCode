


target_cubes = { 'red': 12, 'green': 13, 'blue': 14}

result_part1 = 0 
with open('XmasOfCode2023/Day2/Day2Input.txt', 'r') as file:
    for line in file:
        # Process each line
        game_id = int(line.split(':')[0].split(' ')[1])

        game = line.split(':')[1]
        subsets = game.split(';')
        subsets_valid = []
        
        for subset in subsets:
            cubes = subset.split(',')
            subset_cubes = {cube.strip().split(' ')[1]: int(cube.strip().split(' ')[0]) for cube in cubes}
            valid_subset = all([val <= target_cubes[key] for key,val in subset_cubes.items()])
            subsets_valid.append(valid_subset)
        
        valid_game = all(subsets_valid)

        if valid_game:
            print(game_id)
            result_part1 += game_id

print(result_part1)

# part 2
result_part2 = 0 
with open('XmasOfCode2023/Day2/Day2Input.txt', 'r') as file:
    for line in file:
        # Process each line
        game_id = int(line.split(':')[0].split(' ')[1])

        game = line.split(':')[1]
        subsets = game.split(';')
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
                
        for subset in subsets:
            cubes = subset.split(',')
            subset_cubes = {cube.strip().split(' ')[1]: int(cube.strip().split(' ')[0]) for cube in cubes}
            for key,val in subset_cubes.items():
                min_cubes[key] = max(min_cubes[key],val )
        power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue'] 
        print(power)
        result_part2 += power

print(result_part2)



