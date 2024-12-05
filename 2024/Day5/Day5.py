




with open('2024/Day5/Day5Input.txt', 'r') as f:
    puzzle = f.read()

rules,updates = puzzle.split('\n\n')

rules = rules.split('\n')
updates = updates.split('\n')

r ={}
for rule in rules:
    a,b = rule.split('|')
    curr = r.get(int(a),[])
    curr.append(int(b))
    r[int(a)] = curr

def fix_pages(b_update):
    i = 0
    while i != len(b_update):
        page = b_update[i]
        for j,page2 in enumerate(b_update[(i+1):]):
            if page in r.get(page2,[]):
                b_update = b_update[:i] + b_update[(i+1): (j+i+2)] + [b_update[i]] + b_update[(j+i+2):len(b_update)]
                i -=1
                break
        i += 1
    return b_update

part1 = 0 
part2 = 0 
for update in updates:
    print(update)
    update = [int(x) for x in update.split(',')]
    update_len = len(update)
    mid_page = update[int((update_len-1)/2)]
    update_valid = True
    for i,page in enumerate(update):
        
        for j in update[(i+1):]:
            if page in r.get(j,[]):
                update_valid = False
                break
        if not update_valid:
            break
    if update_valid:
        part1 += mid_page
    else:
        update_fixed = fix_pages(update)
        part2 += update_fixed[int((len(update_fixed)-1)/2)]


print(part1)
print(part2)

    
