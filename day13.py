import math

import modules.aoc as AOC

input = AOC.readDayInput('13')

myEarliestTime = int(input[0])
buses = [ int(bus) if bus != 'x' else bus for bus in input[1].split(',') ]

## FIRST STAR
earliestBusID = None
earliestBusTime = myEarliestTime * myEarliestTime

for busID in buses:
    if (busID == 'x'): continue

    firstBus = int(math.ceil(myEarliestTime / busID)) * busID

    if (firstBus < earliestBusTime):
        earliestBusTime = firstBus
        earliestBusID = busID

AOC.printDayAnswer(1, earliestBusID * (earliestBusTime - myEarliestTime))

## SECOND STAR
def chineseRemainderTheorem(numbers, remainders):
    product = math.prod(numbers)
    productDiv = [ product // num for num in numbers ]

    inverses = [ pow(productDiv[i], numbers[i] - 2, numbers[i]) for i in range(len(productDiv)) ]

    x = 0
    for i in range(len(numbers)):
        x += productDiv[i] * inverses[i] * remainders[i]

    x %= product

    return x

numbers = [buses[0]]
remainders = [0]

for i in range(1, len(buses)):
    if (buses[i] == 'x'): continue

    numbers.append(buses[i])
    remainders.append(buses[i] - i)

AOC.printDayAnswer(2, chineseRemainderTheorem(numbers, remainders))

## To solve the second star puzzle, I used the Chinese Remainder Theorem, after a lot
## of people in the AoC Reddit talking about it. After an hour trying to understand
## it, this video help me A LOT: https://www.youtube.com/watch?v=ru7mWZJlRQg