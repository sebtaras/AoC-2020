f = open("08input.txt")

instructions = []
for line in f:
    instructions.append(line.strip())

acc = 0
next_op = 0
performed = []
while(True):
    if next_op in performed:
        print(acc)
        break
    performed.append(next_op)
    temp = instructions[next_op].split(" ")
    instruction = temp[0]
    value = int(temp[1])
    if instruction == "nop":
        next_op += 1
    elif instruction == "acc":
        next_op += 1
        acc += value
    elif instruction == "jmp":
        next_op += value

acc = 0
next_op = 0
performed = []

while(True):
    if next_op == len(instructions):
        print(acc)
        break
    performed.append(next_op)
    temp = instructions[next_op].split(" ")
    instruction = temp[0]
    value = int(temp[1])
    if instruction == "nop":
        if next_op + 1 in performed:
            instructions[next_op] = "jmp " + temp[1]
            next_op += value
        else:
            next_op += 1
    elif instruction == "acc":
        next_op += 1
        acc += value
    elif instruction == "jmp":
        if next_op + value in performed:
            instructions[next_op] = "nop " + temp[1]
            next_op += 1
        else:
            next_op += value