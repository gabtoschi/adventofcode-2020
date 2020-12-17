import modules.aoc as AOC

input = AOC.groupInput(AOC.readDayInput('16'))

fields = dict()
for line in input[0]:
    fieldName, rawRanges = line.split(': ')
    rawRanges = rawRanges.split(' or ')
    fieldRanges = []

    for rawRange in rawRanges:
        minRange, maxRange = rawRange.split('-')
        fieldRanges.append((int(minRange), int(maxRange)))

    fields[fieldName] = fieldRanges

mapTicket = lambda ticketLine: [ int(num) for num in ticketLine.split(',') ]
myTicket = mapTicket(input[1][1])
nearbyTickets = [ mapTicket(ticket) for ticket in input[2][1:] ]

## FIRST STAR
errorRate = 0
validTickets = []

for ticket in nearbyTickets:
    validTicket = True

    for value in ticket:
        validValue = False

        for ranges in fields.values():
            if ranges[0][0] <= value <= ranges[0][1] or ranges[1][0] <= value <= ranges[1][1]:
                validValue = True
                break

        if not validValue:
            errorRate += value
            validTicket = False

    if validTicket: validTickets.append(ticket)

AOC.printDayAnswer(1, errorRate)

## SECOND STAR
matches = dict()

def getMatchListFromField(fieldName):
    ranges = fields[fieldName]
    matchList = []

    for i in range(len(fields)):
        matched = True

        for ticket in validTickets:
            if not (ranges[0][0] <= ticket[i] <= ranges[0][1] or ranges[1][0] <= ticket[i] <= ranges[1][1]):
                matched = False
                break

        if matched: matchList.append(i)

    return matchList

for fieldName in fields:
    matches[fieldName] = getMatchListFromField(fieldName)

missingFields = list(fields.keys())
foundFields = dict()

while missingFields:
    for field in missingFields:
        if (len(matches[field]) == 1):
            foundFields[field] = matches[field][0]

            for matchList in matches.values():
                if foundFields[field] in matchList: matchList.remove(foundFields[field])

            missingFields.remove(field)

answer = 1
for field in foundFields:
    if 'departure' in field: answer *= myTicket[foundFields[field]]

AOC.printDayAnswer(2, answer)