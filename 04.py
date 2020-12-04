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

passport_required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

counter = 0
for passport in passports:
    if all(keys in passport.keys() for keys in passport_required_fields):
        counter += 1

#Part 1
print(counter)