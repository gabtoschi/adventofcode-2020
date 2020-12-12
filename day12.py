import modules.aoc as AOC

input = AOC.readDayInput('12')

directions = {
    'N': (0, 1),
    'S': (0, -1),
    'W': (-1, 0),
    'E': (1, 0)
}


## FIRST STAR
shipRotations = {
    'L': lambda a, b, n: (a - b + n) % n,
    'R': lambda a, b, n: (a + b) % n,
}

indexToDirection = ['N', 'E', 'S', 'W']

coords = [0, 0]
direction = indexToDirection.index('E')

for command in input:
    action = command[:1]
    value = int(command[1:])

    if action == 'F':
        action = indexToDirection[direction]

    if action in directions.keys():
        coords[0] += value * directions[action][0]
        coords[1] += value * directions[action][1]
    else:
        direction = shipRotations[action](direction, value // 90, len(indexToDirection))

AOC.printDayAnswer(1, sum([abs(n) for n in coords]))

## SECOND STAR
ship = [0, 0]
waypoint = [10, 1]

waypointRotations = {
    'L': lambda x, y: [y * -1, x],
    'R': lambda x, y: [y, x * -1],
}

for command in input:
    action = command[:1]
    value = int(command[1:])

    if action in directions.keys():
        waypoint[0] += value * directions[action][0]
        waypoint[1] += value * directions[action][1]
    elif action in waypointRotations.keys():
        for i in range(value // 90):
            waypoint = waypointRotations[action](waypoint[0], waypoint[1])
    else:
        ship[0] += value * waypoint[0]
        ship[1] += value * waypoint[1]

AOC.printDayAnswer(2, sum([abs(n) for n in ship]))