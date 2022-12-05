import re

INPUTFILE = "2022/data.txt"

with open(INPUTFILE, "r") as file:
    data = file.read().split("\n")

cargo = []

for line in data:
    listline = [*line]

    for i in reversed(range(3, len(listline), 4)):
        listline.pop(i)
    for i in reversed(range(0, len(listline), 3)):
        listline.pop(i)
    for i in reversed(range(1, len(listline), 2)):
        listline.pop(i)

    if listline[0] == "1":
        break

    cargo.append(listline)






stacks = []

for i in range(len(cargo[0])):
    stacks.append([])
    for j in reversed(range(len(cargo))):
        stacks[i].append(cargo[j][i])

for stack in stacks:
    for i in reversed(range(len(stack))):
        if stack[i] == " ":
            stack.pop(i)

startInstructions = False
for line in data:
    if len(line) == 0:
        startInstructions = True
        continue
    if not startInstructions:
        continue

    instructions = re.findall(r'\d+', line)

    for iters in range(int(instructions[0])):
        crate = stacks[int(instructions[1])-1].pop(-1)
        stacks[int(instructions[2])-1].append(crate)

print("Part 1: ", end="")
for stack in stacks:
    print(stack[-1], end="")
print()






stacks = []

for i in range(len(cargo[0])):
    stacks.append([])
    for j in reversed(range(len(cargo))):
        stacks[i].append(cargo[j][i])

for stack in stacks:
    for i in reversed(range(len(stack))):
        if stack[i] == " ":
            stack.pop(i)

startInstructions = False
for line in data:
    if len(line) == 0:
        startInstructions = True
        continue
    if not startInstructions:
        continue

    instructions = re.findall(r'\d+', line)
    
    idx = len(stacks[int(instructions[1])-1]) - int(instructions[0])
    for _ in range(int(instructions[0])):
        crate = stacks[int(instructions[1])-1].pop(idx)
        stacks[int(instructions[2])-1].append(crate)

print("Part 2: ", end="")
for stack in stacks:
    print(stack[-1], end="")
print()