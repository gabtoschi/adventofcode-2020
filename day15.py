import modules.aoc as AOC

input = AOC.readDayInput('15')[0].split(',')
input = [ int(x) for x in input ]

def memoryGame(starters, lastNumber):
    occurences = dict()
    spoken = starters[:]

    for i in range(len(spoken)):
        occurences[spoken[i]] = [i]

    for i in range(len(spoken), lastNumber):
        lastSpoken = spoken[i - 1]

        if len(occurences[lastSpoken]) == 1:
            spoken.append(0)
        else:
            spoken.append(occurences[lastSpoken][-1] - occurences[lastSpoken][-2])

        if spoken[i] in occurences:
            occurences[spoken[i]].append(i)
        else:
            occurences[spoken[i]] = [i]

    return spoken[-1]

## FIRST STAR
AOC.printDayAnswer(1, memoryGame(input, 2020))

## SECOND STAR
AOC.printDayAnswer(2, memoryGame(input, 30000000))