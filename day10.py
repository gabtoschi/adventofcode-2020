import modules.aoc as AOC

input = AOC.readDayInput('10', True)
input.sort()

## FIRST STAR
differences = [0, 0, 1]
differences[input[0] - 1] += 1

for i in range(1, len(input)):
    differences[input[i] - input[i-1] - 1] += 1

AOC.printDayAnswer(1, differences[0] * differences[2])

## SECOND STAR
input = [0] + input
possibilities = [None] * len(input)
maxJolt = max(input)

def calcPossibilities(i):
    if (input[i] == maxJolt):
        return 1

    count = 0

    for next in range(i+1, i+4):
        if next < len(input) and (input[next] - input[i]) <= 3:
            if possibilities[next] is None:
                count += calcPossibilities(next)
            else:
                count += possibilities[next]

    possibilities[i] = count
    return count

calcPossibilities(0)
AOC.printDayAnswer(2, possibilities[0])