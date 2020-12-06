import modules.aoc as AOC

input = AOC.groupInput(AOC.readDayInput('06'))

def createLetterDict():
    letterDict = dict()

    for i in range(ord('a'), ord('z') + 1):
        letterDict[chr(i)] = 0

    return letterDict

# FIRST STAR
totalAnswers = 0

for group in input:
    groupSet = set()

    for personAnswers in group:
        [groupSet.add(answer) for answer in personAnswers]

    totalAnswers += len(groupSet)

AOC.printDayAnswer(1, totalAnswers)

# SECOND STAR
totalAnswers = 0

for group in input:
    frequency = createLetterDict()

    for personAnswers in group:
        for answer in personAnswers:
            frequency[answer] += 1

    frequency = { letter:freq for (letter,freq) in frequency.items() if freq == len(group) }
    totalAnswers += len(frequency)

AOC.printDayAnswer(2, totalAnswers)
