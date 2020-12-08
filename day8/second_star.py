data = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        instr = line.strip().split(' ')
        data.append((instr[0], int(instr[1])))

def execute_program(index, acc, prog):
    while index < len(prog):
        if index in executed_instructions:
            return
        executed_instructions.add(index)
        instr = prog[index]
        if instr[0] == 'nop':
            next_index = index + 1
        elif instr[0] == 'acc':
            acc += instr[1]
            next_index = index + 1
        else:
            next_index = index + instr[1]
        execute_program(next_index, acc, prog)
    print(acc)
    exit(4)

for index, instruction in enumerate(data):
    executed_instructions = set()
    prog = data.copy()
    if prog[index][0] == 'jmp':
        prog[index] = ('nop', instruction[1])
    elif prog[index][0] == 'nop':
        prog[index] = ('jmp', instruction[1])
    execute_program(0, 0, prog)
