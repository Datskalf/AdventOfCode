INPUTFILE = "2022/data.txt"

with open(INPUTFILE, "r") as file:
    data = file.read()



points = {
    "part1": {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6
    },
    "part2": {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7
    }
}



part1 = 0
part2 = 0

for line in data.split("\n"):
    part1 += points["part1"][line]
    part2 += points["part2"][line]

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")