INPUTFILE = "2022/data.txt"

with open(INPUTFILE, "r") as file:
    data = file.read().split("\n")

pairs = [d.split(",") for d in data]

fullyContainedPairCount = 0
anyOverlapCount = 0

for pair in pairs:
    elf1Sections = [int(p) for p in pair[0].split("-")]
    elf2Sections = [int(p) for p in pair[1].split("-")]

    if elf1Sections[0] >= elf2Sections[0] and elf1Sections[1] <= elf2Sections[1]:
        fullyContainedPairCount += 1
    elif elf1Sections[0] <= elf2Sections[0] and elf1Sections[1] >= elf2Sections[1]:
        fullyContainedPairCount += 1
    
    if elf1Sections[0] in range(elf2Sections[0], elf2Sections[1]+1):
        anyOverlapCount += 1
    elif elf1Sections[1] in range(elf2Sections[0], elf2Sections[1]+1):
        anyOverlapCount += 1
    elif elf2Sections[0] in range(elf1Sections[0], elf1Sections[1]+1):
        anyOverlapCount += 1
    elif elf2Sections[1] in range(elf1Sections[0], elf1Sections[1]+1):
        anyOverlapCount += 1
    

print(f"Part 1: {fullyContainedPairCount}")
print(f"Part 2: {anyOverlapCount}")