INPUTFILE = "2022/Day 1/data.txt"

with open(INPUTFILE, "r") as file:
    data = file.read()

sums = []

index = 0
for line in data.split('\n'):
    if len(line) == 0:
        index += 1
        continue
    if len(sums) == index:
        sums.append(0)
    sums[index] += int(line)

sums.sort(reverse=True)
print(f"Part 1: {sums[0]}")
print(f"Part 2: {sums[0] + sums[1] + sums[2]}")