import re

import modules.aoc as AOC

input = AOC.readDayInput('04')

# FIRST STAR
passports = []
currentPassport = {}

for line in input:
    if line:
        passportData = line.split()

        for info in passportData:
            field, value = info.split(':', 1)

            if field != 'cid':
                currentPassport[field] = value
    else:
        passports.append(currentPassport)
        currentPassport = {}

passports.append(currentPassport)

requiredFields = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
validPassports = []

for passport in passports:
    if len(set(passport.keys()) & set(requiredFields)) == len(requiredFields):
        validPassports.append(passport)

AOC.printDayAnswer(1, len(validPassports))

# SECOND STAR
validations = {
    'byr': lambda value: 1920 <= int(value) <= 2002,
    'iyr': lambda value: 2010 <= int(value) <= 2020,
    'eyr': lambda value: 2020 <= int(value) <= 2030,
    'hgt': lambda value: ("in" in value and 59 <= int(re.sub(r"in", '', value)) <= 76) or ("cm" in value and 150 <= int(re.sub(r"cm", '', value)) <= 193),
    'hcl': lambda value: re.match(r"^#[0-9a-f]{6}$", value),
    'ecl': lambda value: value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda value: re.match(r"^\d{9}$", value),
}

fullValidPassports = []

for passport in validPassports:
    isValid = True

    for field in sorted(passport.keys()):
        isValid = isValid and validations[field](passport[field])

    if isValid: fullValidPassports.append(passport)

AOC.printDayAnswer(2, len(fullValidPassports))