#Day 04

with open('./04.txt') as myinput:
    inputlines = myinput.readlines()

inputlines = ''.join(line.replace(' ','\n') for line in inputlines).splitlines()
inputlines.append('')

#Part 1

passport_required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passports = []
passport = {}
for line in inputlines:
    if line:
        k, v = line.split(':')
        passport[k] = v
    else:
        if all(k in passport.keys() for k in passport_required_fields):
            passports.append(passport)
        passport = {}

print(len(passports))

#Part 2

valid_chars = '0123456789abcdef'
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

counter = 0
for passport in passports:
    if int(passport['byr']) in range(1920, 2003):
        if int(passport['iyr']) in range(2010, 2021):
            if int(passport['eyr']) in range(2020, 2031):
                if passport['hgt'][-2:] == 'cm' and int(passport['hgt'][:-2]) in range(150, 194) or passport['hgt'][-2:] == 'in' and int(passport['hgt'][:-2]) in range(59, 77):
                    if passport['hcl'][0] == '#' and len(passport['hcl']) == 7 and all(chars in valid_chars for chars in passport['hcl'][1:]):
                        if passport['ecl'] in valid_ecl:
                            if len(passport['pid']) == 9:
                                counter += 1

print(counter)
