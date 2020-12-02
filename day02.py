import re

import modules.aoc as AOC

input = AOC.readDayInput('02')

# FIRST STAR
regex = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")

correctWords = 0

for password in input:
    groups = regex.match(password).groups()

    min = int(groups[0])
    max = int(groups[1])
    letter = groups[2]
    word = groups[3]
    counter = 0

    for let in word:
        if (let == letter):
            counter += 1

    if (counter >= min and counter <= max):
        correctWords += 1

AOC.printDayAnswer(1, correctWords)

# SECOND STAR
correctWords = 0

for password in input:
    groups = regex.match(password).groups()

    index1 = int(groups[0]) - 1
    index2 = int(groups[1]) - 1
    letter = groups[2]
    word = groups[3]
    analysis = 0

    if (word[index1] == letter): analysis += -1
    if (word[index2] == letter): analysis += +1

    correctWords += abs(analysis)

AOC.printDayAnswer(2, correctWords)