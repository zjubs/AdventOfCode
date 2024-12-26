
with open('2024/Day24/Day24Input.txt', 'r') as f:
    initial,wires_in = f.read().split('\n\n')

outputs = {}
for i in initial.split('\n'):
    a,b = i.split(':')
    outputs[a] = int(b)

wires = {}
for i in wires_in.split('\n'):
    a,b = i.split('->')
    x1,op,x2 = a.split()
    wires[b.strip()] = [(x1,x2),op]


not_seen = set(wires.keys())
seen = set(outputs.keys())

while not_seen:
    for wire,calc in wires.items():
        calc = wires[wire]
        if wire in not_seen and set(calc[0]).issubset(seen):
            match calc[1]:
                case 'OR':
                    outputs[wire] = outputs[calc[0][0]] or outputs[calc[0][1]]
                case 'AND':
                    outputs[wire] = outputs[calc[0][0]] and outputs[calc[0][1]]
                case 'XOR':
                    outputs[wire] = outputs[calc[0][0]] ^ outputs[calc[0][1]]
            seen.add(wire)
            not_seen.remove(wire)

x=1
            
required_keys = sorted([key for key in outputs.keys() if key.startswith("z")],reverse=True)
res = int(''.join([str(outputs[key]) for key in required_keys]),2)
print(f'Part1: {res}')

# part2 

issues = set()
for row in wires_in.split('\n'):

    in1,op,in2,_,out1 = row.split()

    if out1.startswith('z') and op in('AND','OR')and out1 != 'z45':
        print(out1)
        issues.add(out1)

    if op == 'XOR' and not out1.startswith('z') and not (in1.startswith('y') or in1.startswith('x')) and not (in1.startswith('y') or in1.startswith('x')):
        print(out1)
        issues.add(out1)

    if op == 'OR' and (in1.startswith('y') or in1.startswith('x') or in1.startswith('y') or in1.startswith('x')):
        print(out1)
        issues.add(out1)

    if op == 'OR':
        for row2 in wires_in.split('\n'):
            in1_sub,op_sub,in2_sub,_,out1_sub = row2.split()
            if out1_sub in (in1, in2) and op_sub != 'AND':
                print(out1_sub)
                #print(out1)
                issues.add(out1)
    
    if op == 'XOR':
        for row2 in wires_in.split('\n'):
            in1_sub,op_sub,in2_sub,_,out1_sub = row2.split()
            if out1_sub in (in1, in2) and op_sub == 'AND':
                print(out1_sub)
                #print(out1)
                issues.add(out1_sub)





# The above gave some additional issues, which are related to other swapped wires
# but from that could infer the correct answer
