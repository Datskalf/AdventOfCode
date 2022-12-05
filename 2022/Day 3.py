INPUTFILE = "2022/data.txt"

import string

with open(INPUTFILE, "r") as file:
    data = file.read()

totalPriority = 0
rucksacks = []
for dataSplit in data.split("\n"):
    midpoint = int(len(dataSplit)/2)

    rucksack = {
        "BothCompartments": dataSplit,
        "FirstCompartment": dataSplit[:midpoint],
        "SecondCompartment": dataSplit[midpoint:],
        "Priority": 0
    }

    for item in rucksack["FirstCompartment"]:
        if item in rucksack["SecondCompartment"]:
            rucksack["Priority"] = string.ascii_letters.index(item) + 1
            break

    rucksacks.append(rucksack)
    totalPriority += rucksack["Priority"]

print(f"Part 1: {totalPriority}")



totalGroupPriority = 0
for index in range(0, len(rucksacks), 3):
    for character in rucksacks[index]["BothCompartments"]:
        if character in rucksacks[index+1]["BothCompartments"] and character in rucksacks[index+2]["BothCompartments"]:
            totalGroupPriority += string.ascii_letters.index(character) + 1
            break

print(f"Path 2: {totalGroupPriority}")