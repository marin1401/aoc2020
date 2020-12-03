#Day 03

with open('./03.txt') as myinput:
    inputlines = myinput.readlines()

inputlines = [line.replace('.', '0').replace('#', '1').replace('\n', '') for line in inputlines]
toboggan = [list(map(int, i)) for i in inputlines]

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
trees = []
trees_product = 1

for slope in slopes:
    position = 0
    counter = 0
    if slope[1] > 1:
        del toboggan[1::slope[1]] #this is wrong, but simple
    for row in toboggan:
        if position < len(row) - slope[0]:
            if row[position] == 1:
                counter += 1
        for i in range(slope[0] + 1):
            if position == len(row) - i:
                if row[position] == 1:
                    counter += 1
                position = -i
        position += slope[0]
    trees.append(counter)
    trees_product = trees_product * counter

#Part 1
print(trees[1])

#Part 2
print(trees_product)
