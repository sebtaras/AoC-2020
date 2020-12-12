def execute(instructions):
    acc = 0
    next_op = 0
    performed = []
    while(True):
        if next_op in performed:
            return False
        performed.append(next_op)
        if next_op == len(instructions):
            print(acc)
            return True
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

f = open("08input.txt")

instructions = []
for line in f:
    instructions.append(line.strip())

acc = 0
next_op = 0
performed = []
while(True):
    if next_op in performed or next_op == len(instructions):
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


potential = list()

for i in instructions:
    if "nop" in i:
        potential.append(1)
    elif "jmp" in i:
        potential.append(2)
    else:
        potential.append(0)

for i in range(0, len(potential)):
    if potential[i] == 0:
        continue
    elif potential[i] == 1:    #replace nop with jmp
        new_instructions = instructions[:]
        temp = new_instructions[i].split(" ")
        new_instructions[i] = "jmp " + temp[1]
        if execute(new_instructions):
            break
    elif potential[i] == 2:
        new_instructions = instructions[:]
        temp = new_instructions[i].split(" ")
        new_instructions[i] = "nop " + temp[1]
        if execute(new_instructions):
            break
