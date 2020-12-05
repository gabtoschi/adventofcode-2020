import re

import modules.aoc as AOC

def getBinaryFromInput(line):
    line = re.sub(r"[F|L]", '0', line)
    return re.sub(r"[B|R]", '1', line)

input = [getBinaryFromInput(line) for line in AOC.readDayInput('05')]
seatIDs = [int(seat, base=2) for seat in input]

## FIRST STAR
AOC.printDayAnswer(1, max(seatIDs))

## SECOND STAR
seatIDs.sort()

for i in range(len(seatIDs) - 1):
    if seatIDs[i] + 2 == seatIDs[i+1]:
        AOC.printDayAnswer(2, seatIDs[i] + 1)
        break