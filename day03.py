import modules.aoc as AOC

input = AOC.readDayInput('03')

tree = '#'

def checkTrees(map, right, down):
    x = 0
    xMax = len(map[0])
    trees = 0

    for y in range(down, len(map), down):
        x = (x + right) % xMax

        if (map[y][x] == tree): trees += 1

    return trees

# FIRST STAR
allTrees = checkTrees(input, 3, 1)
AOC.printDayAnswer(1, allTrees)

# SECOND STAR
slopes = [
    [1, 1], [5, 1], [7, 1], [1, 2]
]

for slope in slopes:
    allTrees *= checkTrees(input, slope[0], slope[1])

AOC.printDayAnswer(2, allTrees)

