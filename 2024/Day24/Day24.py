
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