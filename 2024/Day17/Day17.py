import re

with open('2024/Day17/Day17Input.txt' ,'r') as f:
    puzzle = f.read()

reg_init,prog_init = puzzle.split('\n\n')
pattern = r'\d+'

#reg
a,b,c = [*map(int,re.findall(pattern, reg_init))]

#prog
prog = [*map(int,prog_init.split(':')[1].strip().split(','))]
opcodes,operands = prog[0::2], prog[1::2]


def get_operand_val(operand):
    match operand:
        case x if x in (1, 2, 3):
            return operand
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c


def apply_inst(opcode,operand,combo,i,a,b,c):
    match opcode:
        case 0: #adv
            a = a //(2**combo)
        case 1: #bxl
            b = b ^ operand
        case 2: #bxl
            b = combo % 8
        case 3: #jnz
            if a != 0:
                i = int(operand / 2 - 1)
                # need to not jump for next instruction()
        case 4: #bxc
            b = b ^ c
        case 5: #out
            output.append(combo % 8)
        case 6: #bdv
            b = a //(2**combo)
        case 7: #bxl
            c = a //(2**combo)
    return i,a,b,c

output = []
i = 0 # need to use this
while i < len(opcodes):
    opcode, operand = opcodes[i],operands[i]
    combo = get_operand_val(operand)
    i,a,b,c = apply_inst(opcode,operand,combo,i,a,b,c)

    i += 1


part1 = ','.join([str(x) for x in output])
print(f'Part1: {part1}')




