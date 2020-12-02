def readDayInput(day, toInt = False):
    inputFile = open(f'inputs/day{day}.dat', 'r')

    rawLines = inputFile.readlines()
    lines = []

    for rawLine in rawLines:
        lineData = rawLine.strip()

        if (toInt):
            lineData = int(lineData)

        lines.append(lineData)

    inputFile.close()

    return lines

def printDayAnswer(star, answer):
    print(f'Star #{star}: {answer}')