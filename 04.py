#Day 04

with open('./04.txt') as myinput:
    inputlines = myinput.readlines()

inputlines = ''.join(line.replace(' ','\n') for line in inputlines).splitlines()

passports = []
passport_data = {}
for line in inputlines:
    if len(line) > 0:
        key, val = line.split(':')
        passport_data[key] = val
    elif len(line) == 0:
        passports.append(passport_data)
        passport_data = {}
passports.append(passport_data)


#Part 1

passport_required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

counter = 0
valid_passports = []
for passport in passports:
    if all(keys in passport.keys() for keys in passport_required_fields):
        counter += 1
        valid_passports.append(passport)

print(counter)

#Part 2

invalid_chars = 'ghijklmnopqrstuvwxyz'
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

for passport in valid_passports:
    for key, value in passport.items():
        if key == 'byr':
            if int(value) < 1920 or int(value) > 2002:
                passport[key] = 'invalid'
        if key == 'iyr':
            if int(value) < 2010 or int(value) > 2020:
                passport[key] = 'invalid'
        if key == 'eyr':
            if int(value) < 2020 or int(value) > 2030:
                passport[key] = 'invalid'
        if key == 'hgt':
            if value[-2:] == 'cm':
                if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                    passport[key] = 'invalid'
            elif value[-2:] == 'in':
                if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                    passport[key] = 'invalid'
            else:
                passport[key] = 'invalid'
        if key == 'hcl':
            if value[0] != '#' or len(value) != 7 or any(chars in invalid_chars for chars in value[1:]):
                passport[key] = 'invalid'
        if key == 'ecl':
            if value not in valid_ecl:
                passport[key] = 'invalid'
        if key == 'pid':
            if len(value) != 9:
                passport[key] = 'invalid'

counter = 0
for passport in valid_passports:
    if 'invalid' not in passport.values():
        counter += 1

print(counter)
