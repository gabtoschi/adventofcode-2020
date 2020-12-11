import modules.aoc as AOC

input = [list(line) for line in AOC.readDayInput('11')]

occupiedSeat = '#'
emptySeat = 'L'
floor = '.'

lenX = len(input[0])
lenY = len(input)

positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def getOccupiedInEquilibrium(seats, getVisibleOccupied, becomeEmptyMin = 4):
    oldSeats = None
    newSeats = [line[:] for line in seats]
    changes = -1

    while changes != 0:
        oldSeats = [line[:] for line in newSeats]
        changes = 0

        for y in range(lenY):
            for x in range(lenX):
                if (oldSeats[y][x] == floor): continue

                visible = getVisibleOccupied(oldSeats, x, y)

                if oldSeats[y][x] == emptySeat and visible == 0:
                    newSeats[y][x] = occupiedSeat
                    changes += 1
                elif oldSeats[y][x] == occupiedSeat and visible >= becomeEmptyMin:
                    newSeats[y][x] = emptySeat
                    changes += 1

    return sum([line.count(occupiedSeat) for line in newSeats])

## FIRST STAR
def getAdjacentOccupied(seats, x, y):
    occupied = 0

    for pos in positions:
        adjX = x + pos[0]
        adjY = y + pos[1]

        if (0 <= adjX < lenX and 0 <= adjY < lenY and seats[adjY][adjX] == occupiedSeat):
            occupied += 1

    return occupied

AOC.printDayAnswer(1, getOccupiedInEquilibrium(input, getAdjacentOccupied))

## SECOND STAR
def getVisibleOccupied(seats, x, y):
    occupied = 0

    for pos in positions:
        visX = x
        visY = y

        while 0 <= visX < lenX and 0 <= visY < lenY:
            visX += pos[0]
            visY += pos[1]

            if 0 <= visX < lenX and 0 <= visY < lenY:
                visibleSeat = seats[visY][visX]

                if visibleSeat == floor: continue
                if visibleSeat == occupiedSeat: occupied += 1

                break

    return occupied

AOC.printDayAnswer(2, getOccupiedInEquilibrium(input, getVisibleOccupied, 5))



