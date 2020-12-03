#Day 02

with open('./03.txt') as myinput:
    inputlines = myinput.readlines()

inputlines = [line.replace('.', '0').replace('#', '1').replace('\n', '') for line in inputlines]
toboggan = [list(map(int, i)) for i in inputlines]

position = 0
counter = 0
for row in toboggan:
    if position < len(row)-3:
        if row[position] == 1:
            counter += 1
    elif position == len(row)-3:
        if row[position] == 1:
            counter += 1
        position = -3
    elif position == len(row)-2:
        if row[position] == 1:
            counter += 1
        position = -2
    elif position == len(row)-1:
        if row[position] == 1:
            counter += 1
        position = -1
    elif position == len(row):
        if row[position] == 1:
            counter += 1
        position = 0
    position += 3

print(counter)