import re
from pprint import pprint

with open("2022/data.txt") as file:
    data = file.read().split("\n")

filesize = {}
parent_directories = []
current_directory=["/"]


def updateFilesize(size, file):
    if file in filesize:
        filesize[file] += int(size)
    else:
        filesize[file] = int(size)


for line in data[1:]:
    linspl = line.split(" ")
    if linspl[1] == "cd":
        if linspl[2] == "..":
            current_directory[0] = parent_directories.pop(-1)
        else:
            parent_directories.append(current_directory[0])
            current_directory[0]=current_directory[0] + "/" + linspl[2]

    elif re.search(r"\d+", linspl[0]):
        updateFilesize(linspl[0], current_directory[0])
        for parent in parent_directories:
            updateFilesize(linspl[0], parent)

print("Part 1: " + str(sum(list(filter(lambda size: size <= 100000, filesize.values())))))



threshold = 40000000
requiredSize = filesize['/'] - threshold

currentbest = []

for key in filesize.keys():
    val = filesize[key]
    if len(currentbest) == 0:
        currentbest = [key, val]
        continue
    if val > requiredSize and val < currentbest[1]:
        currentbest = [key, val]

print(f"Part 2: {currentbest[1]}")