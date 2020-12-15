import modules.aoc as AOC

input = AOC.readDayInput('14')

toBinary = lambda n, b: ('{:0' + str(b) + 'b}').format(n)

## FIRST STAR
memory = dict()
currentMaskTo1 = None
currentMaskTo0 = None

for line in input:
    command, value = line.split(' = ')

    if (command == 'mask'):
        currentMaskTo1 = int(value.replace('X', '0'), base=2)
        currentMaskTo0 = int(value.replace('X', '1'), base=2)
        continue

    command = command.replace('mem[', '').replace(']', '')
    value = int(value)

    memory[command] = (value | currentMaskTo1) & currentMaskTo0

AOC.printDayAnswer(1, sum(memory.values()))

## SECOND STAR
memory = dict()
currentMask = ''

for line in input:
    command, value = line.split(' = ')

    if (command == 'mask'):
        currentMask = value
        continue

    command = int(command.replace('mem[', '').replace(']', ''))
    value = int(value)

    commandBin = list(toBinary(command, 36))
    for i in range(len(currentMask)):
        if (currentMask[i] != '0'): commandBin[i] = currentMask[i]
    commandBin = ''.join(commandBin)

    floatingIndices = []
    for i in range(len(commandBin)):
        if commandBin[i] == 'X': floatingIndices.append(i)

    possibilities = pow(2, len(floatingIndices))

    for i in range(possibilities):
        floatingSubs = toBinary(i, len(floatingIndices))
        commandFinal = list(commandBin)

        for j in range(len(floatingIndices)):
            commandFinal[floatingIndices[j]] = floatingSubs[j]

        memory[int(''.join(commandFinal))] = value

AOC.printDayAnswer(2, sum(memory.values()))

