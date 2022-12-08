import math

with open("2022/data.txt") as file:
    filedata = file.read().split('\n')

data = [[*n] for n in filedata]
isVisible = []

def checkVisibleFromOutside(x, y):
    treeHeight = data[x][y]

    runResult = []
    for i in range(x):
        if not treeHeight > data[i][y]:
            runResult.append(False)
            break
    for i in range(y):
        if not treeHeight > data[x][i]:
            runResult.append(False)
            break
    for i in range(x+1, len(data)):
        if not treeHeight > data[i][y]:
            runResult.append(False)
            break
    for i in range(y+1, len(data[0])):
        if not treeHeight > data[x][i]:
            runResult.append(False)
            break
    
    return runResult.count(False) < 4
    

for x in range(len(data)):
    isVisible.append([])
    for y in range(len(data[0])):
        isVisible[x].append(checkVisibleFromOutside(x, y))

print(f"Part 1: {sum([x.count(True) for x in isVisible])}")


maxValue = 0
for x in range(len(data)):
    for y in range(len(data[0])):
        values = []
        treeHeight = data[x][y]
        
        length = 0
        for i in reversed(range(x)):
            length += 1
            if data[i][y] >= treeHeight:
                break
        values.append(length)

        length = 0
        for i in reversed(range(y)):
            length += 1
            if data[x][i] >= treeHeight:
                break
        values.append(length)
            
        length = 0
        for i in range(x+1, len(data)):
            length += 1
            if data[i][y] >= treeHeight:
                values[-1] = i-x
                break
        values.append(length)
            
        length = 0
        for i in range(y+1, len(data[0])):
            length += 1
            if data[x][i] >= treeHeight:
                break
        values.append(length)

        prod = math.prod(values)
        if prod > maxValue:
            maxValue = prod

print(f"Part 2: {maxValue}")