import re
import copy

INPUTFILE = "2022/data.txt"

with open(INPUTFILE, "r") as file:
    data = file.read().split("\n")

cargo = []
instructions = []
stillInstruction = True

for line in reversed(data):
    listline = [*line]

    if len(listline) == 0:
        stillInstruction = False
        continue
    if listline[0] == " ":
        continue

    if stillInstruction:
        instructions.append([int(n) for n in re.findall('\d+', line)])
    else:
        cargo.append(listline[1::4])

load = []
for i, layer in enumerate(cargo):
    for j, element in enumerate(layer):
        if len(load) < j+1:
            load.append([])
        if element == " ":
            continue
        load[j].append(element)

instructions.reverse()




rearrangedLoad = copy.deepcopy(load)

for instruction in instructions:
    ins = [instruction[0], instruction[1]-1, instruction[2]-1]
    
    for _ in range(ins[0]):
        crate = rearrangedLoad[ins[1]].pop(-1)
        rearrangedLoad[ins[2]].append(crate)

result = "".join([stack[-1] for stack in rearrangedLoad])
print(f"Part 1: {result}")



rearrangedLoad = copy.deepcopy(load)

for instruction in instructions:
    ins = [instruction[0], instruction[1]-1, instruction[2]-1]
    
    idx = len(rearrangedLoad[ins[1]])-ins[0]
    for _ in range(ins[0]):
        crate = rearrangedLoad[ins[1]].pop(idx)
        rearrangedLoad[ins[2]].append(crate)

result = "".join([stack[-1] for stack in rearrangedLoad])
print(f"Part 2: {result}")