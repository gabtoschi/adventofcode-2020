import itertools

import modules.aoc as AOC

input = AOC.readDayInput('09', True)
preamble = 25

## FIRST STAR
for i in range(preamble, len(input)):
    if not any([sum(comb) == input[i] for comb in itertools.combinations(input[i-preamble:i], 2)]):
        invalid = input[i]
        AOC.printDayAnswer(1, input[i])
        break

## SECOND STAR
start = 0
end = 1
weakSum = input[start] + input[end]

while (weakSum != invalid):
    if (weakSum < invalid):
        end += 1
        weakSum += input[end]
    elif (weakSum > invalid):
        while (weakSum > invalid and start < end):
            weakSum -= input[start]
            start += 1

weakList = input[start:end+1]
AOC.printDayAnswer(2, min(weakList) + max(weakList))