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


# TODO use match case instead of if

def get_operand_val(operand):
    match operand:
        case x if x in (1, 2, 3):
            return operand
        case 4:
            return reg['A']
        case 5:
            return reg['B']
        case 6:
            return reg['C']


def apply_inst(opcode,operand,combo,i):
    match opcode:
        case 0: #adv
            reg['A'] = reg['A'] //(2**combo)
        case 1: #bxl
            reg['B'] = reg['B'] ^ operand
        case 2: #bxl
            reg['B'] = combo % 8
        case 3: #jnz
            if reg['A'] != 0:
                i = int(operand / 2 - 1)
                # need to not jump for next instruction()
        case 4: #bxc
            reg['B'] = reg['B'] ^ reg['C']
        case 5: #out
            output.append(combo % 8)
        case 6: #bdv
            reg['B'] = reg['A'] //(2**combo)
        case 7: #bxl
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




