INPUTFILE = "2022/data.txt"

with open(INPUTFILE, "r") as file:
    data = file.read()

def findPattern(length):
    chars = []
    for i, char in enumerate(data):   
        chars.append(char)

        if len(chars) >= 4 and len(chars[length*-1:]) == len(set(chars[length*-1:])):
            return i + 1

print(f"Part 1: {findPattern(4)}")
print(f"Part 2: {findPattern(14)}")