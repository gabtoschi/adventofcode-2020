import modules.aoc as AOC

input = AOC.readDayInput('07')
myBag = 'shiny gold bag'

## INPUT PROCESSING
allBags = dict()

for line in input:
    currentBag, bagContentStr = line.split(' contain ')

    currentBag = currentBag.replace('bags', 'bag')
    bagContentList = bagContentStr.rstrip('.').split(',')

    bagContent = dict()
    for content in bagContentList:
        if (content != 'no other bags'):
            amount, color = content.replace('bags', 'bag').split(maxsplit=1)
            bagContent[color] = amount

    allBags[currentBag] = bagContent

## FIRST STAR
contentBags = [myBag]
contentIndex = 0

while (contentIndex < len(contentBags)):
    currentBag = contentBags[contentIndex]

    for bagKey in allBags:
        if currentBag in allBags[bagKey] and bagKey not in contentBags:
            contentBags.append(bagKey)

    contentIndex += 1

AOC.printDayAnswer(1, len(contentBags) - 1)

## SECOND STAR
def countBagsInside(bag):
    if allBags[bag] == {}:
        return 0

    amount = 0
    for insideBagKey in allBags[bag]:
        amountOfThisBag = int(allBags[bag][insideBagKey])
        amount += amountOfThisBag + (countBagsInside(insideBagKey) * amountOfThisBag)

    return amount

AOC.printDayAnswer(2, countBagsInside(myBag))