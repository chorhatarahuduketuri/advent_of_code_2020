data = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        instr = line.strip().split(' ')
        data.append((instr[0], int(instr[1])))

executed_instructions = set()


def loop(idx, a):
    if idx in executed_instructions:
        print(a)
        exit(4)
    executed_instructions.add(idx)
    execute_instruction(idx, a)


def execute_instruction(index, acc):
    instruction = data[index]
    if instruction[0] == 'nop':
        index += 1
        loop(index, acc)
    if instruction[0] == 'acc':
        acc += instruction[1]
        index += 1
        loop(index, acc)
    if instruction[0] == 'jmp':
        index += instruction[1]
        loop(index, acc)


execute_instruction(0, 0)
