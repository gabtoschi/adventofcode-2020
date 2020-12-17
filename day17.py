import itertools
import modules.aoc as AOC

input = AOC.readDayInput('17')
sumCoord = lambda a, b: tuple([ a[i] + b[i] for i in range(len(a)) ])

def bootingCycles(startState, dimensions):
    startGrid = dict()
    startGridZeroes = [0] * (dimensions - 2)

    for i in range(len(startState)):
        for j in range(len(startState[0])):
            startGrid[tuple([i, j] + startGridZeroes)] = startState[i][j]

    neighbors = set(itertools.combinations_with_replacement([-1, 0, 1] * dimensions, dimensions))
    neighbors.remove(tuple([0] * dimensions))

    for i in range(6):
        for cube in list(startGrid.keys()):
            for neighbor in neighbors:
                neighborCoord = sumCoord(cube, neighbor)

                if neighborCoord not in startGrid:
                    startGrid[neighborCoord] = '.'

        newGrid = startGrid.copy()

        for cube in startGrid:
            activatedNeighbors = 0

            for neighbor in neighbors:
                neighborCoord = sumCoord(cube, neighbor)

                if neighborCoord in startGrid and startGrid[neighborCoord] == '#':
                    activatedNeighbors += 1

            if startGrid[cube] == '#' and activatedNeighbors not in [2,3]:
                newGrid[cube] = '.'
            elif startGrid[cube] == '.' and activatedNeighbors == 3:
                newGrid[cube] = '#'

        startGrid = newGrid

    return list(startGrid.values()).count('#')

AOC.printDayAnswer(1, bootingCycles(input, 3)) # FIRST STAR
AOC.printDayAnswer(2, bootingCycles(input, 4)) # SECOND STAR