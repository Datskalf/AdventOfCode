with open("2022/Day 2/data.txt", "r") as file:
    data = file.read()

totalScore = 0

points = {
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

for i, line in enumerate(data.split("\n")):
    roundScore = 0

    roundScore = points[line]
    
    print(f"Game {i}: {roundScore}")
    totalScore += roundScore

print(f"\nTotal score: {totalScore}")