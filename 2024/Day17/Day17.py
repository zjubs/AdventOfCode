import re

with open('2024/Day17/Day17Input.txt' ,'r') as f:
    puzzle = f.read()

#resister
reg_init,prog_init = puzzle.split('\n\n')
reg = {}
pattern = r'\d+'
for let,line in zip(['A','B','C'],reg_init.split('\n')):
    z = re.findall(pattern, line)
    reg[let] = int(re.findall(pattern, line)[0])

prog = [*map(int,prog_init.split(':')[1].strip().split(','))]
opcodes,operands = prog[0::2], prog[1::2]


def get_operand_val(operand):
    if operand in (0,1,2,3):
        return operand
    elif operand == 4:
        return reg['A']
    elif operand == 5:
        return reg['B']
    elif operand == 6:
        return reg['C']


def apply_inst(opcode,operand,combo,i):
    if opcode == 0: #adv
        reg['A'] = reg['A'] //(2**combo)
    elif opcode == 1: #bxl
        reg['B'] = reg['B'] ^ operand
    elif opcode == 2: #bxl
        reg['B'] = combo % 8
    elif opcode == 3: #jnz
        if reg['A'] != 0:
            i = int(operand / 2 - 1)
            # need to not jump for next instruction()
    elif opcode == 4: #bxc
        reg['B'] = reg['B'] ^ reg['C']
    elif opcode == 5: #out
        output.append(combo % 8)
    elif opcode == 6: #bdv
        reg['B'] = reg['A'] //(2**combo)
    elif opcode == 7: #bxl
        reg['C'] = reg['A'] //(2**combo)
    return i

output = []
i = 0 # need to use this
while i < len(opcodes):
    opcode, operand = opcodes[i],operands[i]
    combo = get_operand_val(operand)
    i = apply_inst(opcode,operand,combo,i)

    i += 1


part1 = ','.join([str(x) for x in output])
print(f'Part1: {part1}')




