with open('2025/Day05/input.txt', 'r') as f:
    puzzle_input = f.read()

rs,ids  = puzzle_input.split('\n\n')

rs = rs.split('\n')
ids = ids.split('\n')

result = 0 
for id in ids:
    for r in rs:
        start,end = r.split('-')
        if int(id) >= int(start) and  int(id) <= int(end):
            result +=1
            break

print(result)



def update(x,curr):
    start = x[0]
    end = x[1]
    to_append = True
    for pos,i in enumerate(curr):
        if start < i[0] and end >i[1]: #both
            
            i[0] = start
            i[1] = end
            n = curr.pop(pos)
            update(n,curr)
            to_append = False
            
            break
        if start < i[0] and end >= i[0] and end <= i[1]: #lower
            
            i[0] = start
            n = curr.pop(pos)
            update(n,curr)
            to_append = False
            break
        if start >= i[0] and start <=i[1] and end > i[1]: # upper
            
            i[1] = end
            n = curr.pop(pos)
            update(n,curr)
            to_append = False
            break
        if start >= i[0] and end <=i[1]: # inside
            to_append = False
            break
    if to_append:
        curr.append([start,end])
        



curr = []
for r in rs:
    start,end = r.split('-')
    start = int(start)
    end = int(end)
    if not curr:
        curr.append([start,end])
    else:
        update([start,end],curr)


result2 = 0
for x in curr:
    result2 +=x[1] - x[0] + 1
print(result2)


        

x = 1

