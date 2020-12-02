import modules.aoc as AOC

input = AOC.readDayInput('01', True)
input.sort()

# FIRST STAR
frequency = [None] * 2021

for number in input:
    frequency[number] = True

    if (frequency[abs(number - 2020)]):
        AOC.printDayAnswer(1, number * abs(number - 2020))
        break

# SECOND STAR
right = len(input) - 1
left = 0
mid = 1
sum = -1

while (sum != 2020):
    sum = input[left] + input[mid] + input[right]

    if (sum < 2020):
        mid += 1

    if (sum > 2020):
        if (mid >= right):
            right -= 1
            left = 0
            mid = 1
        else:
            left += 1
            mid = left + 1

AOC.printDayAnswer(2, input[left] * input[mid] * input[right])