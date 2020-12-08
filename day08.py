import copy

import modules.aoc as AOC

input = AOC.readDayInput('08')

## INPUT PROCESSING
def getInstruction(inputLine):
    instruction = dict()

    op, arg = inputLine.split(' ', 1)
    instruction['op'] = op
    instruction['arg'] = int(arg)

    return instruction

instructions = [ getInstruction(line) for line in input ]

## FIRST STAR
def executeBoot(instructions):
    accumulator = 0
    executedIndexes = set()
    index = 0
    looped = False

    while index < len(instructions):
        if index in executedIndexes:
            looped = True
            break

        executedIndexes.add(index)

        if (instructions[index]['op'] == 'acc'):
            accumulator += instructions[index]['arg']

        if (instructions[index]['op'] == 'jmp'):
            index += instructions[index]['arg']
        else:
            index += 1

    return accumulator, looped

acc, looped = executeBoot(instructions)
AOC.printDayAnswer(1, acc)

## SECOND STAR
for i in range(len(instructions)):
    if instructions[i]['op'] != 'acc':
        newInstructions = copy.deepcopy(instructions)
        newInstructions[i]['op'] = 'nop' if newInstructions[i]['op'] == 'jmp' else 'jmp'

        acc, looped = executeBoot(newInstructions)
        if not looped:
            AOC.printDayAnswer(2, acc)
            break