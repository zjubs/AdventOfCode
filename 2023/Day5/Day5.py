
# process data

sections = {}
current_key = None
current_section = []

with open('Day5/Day5Input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line == "":
            # End of current section
            if current_key and current_section:  # Only add non-empty sections
                sections[current_key] = current_section
                current_section = []
            current_key = None  # Reset the key after each blank line
        elif line.endswith(":"):
            # Set a new key when encountering a header line
            current_key = line.rstrip(":")
        elif ':' in line:
            # process seeds line
            current_key = line.split(':')[0] 
            current_section.append([int(num) for num in line.split(':')[1].split()])   

        else:
            # Collect data lines
            current_section.append([int(num) for num in line.split()])

    # Add the last section if there's no trailing blank line in the file
    if current_key and current_section:
        sections[current_key] = current_section

# order based on source
# for each seed, then check if it falls in a category
    # use function for this
    # if not use base mapping

# sort list in each section
for key, value in sections.items():
    sections[key] = sorted(value, key=lambda x: x[1])

#mapping function
def map_to_value(mapping, source_val):
    mapped_val = None
    for map in mapping:
        if source_val in range(map[1], map[1]+ map[2]):
            mapped_val = map[0] + (source_val - map[1])
            break
    if not mapped_val:
        mapped_val = source_val
    
    return mapped_val

# print(map_to_value(sections['seed-to-soil map'],79))

# apply all mappings
def apply_mappings(mappings,x):
    for key,val in sections.items():
        if key != 'seeds':
            x = map_to_value(val,x)
            #print(x)
    return x

#print(apply_mappings(sections,79))

# iterate over each seed
# part1
seeds ={}
for seed in sections['seeds'][0]:

    seeds[seed] = apply_mappings(sections,seed)


print(min(seeds.values()))

# part 2
seeds ={}
for seed in sections['seeds'][0]:

    seeds[seed] = apply_mappings(sections,seed)


print(min(seeds.values()))


    




x = 1
# all_mappings = {} 
# for key,value in sections.items():
#     if key != 'seeds':
#         mapping_category = {}
#         for map in value:
#             current_map = {}
#             mapping_category.append()


