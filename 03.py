#Day 03

with open('./03.txt') as myinput:
    inputlines = myinput.readlines()

toboggan = [line.strip() for line in inputlines]

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
trees = []
trees_product = 1

for slope in slopes:
    position, counter = 0, 0
    for row in toboggan:
        if slope[1] > 1:
            if toboggan.index(row) % slope[1] != 0:
                continue
        if position < len(row) - slope[0]:
            if row[position] == '#':
                counter += 1
        for i in range(slope[0] + 1):
            if position == len(row) - i:
                if row[position] == '#':
                    counter += 1
                position = -i
        position += slope[0]
    trees.append(counter)
    trees_product = trees_product * counter

#Part 1

print(trees[1])

#Part 2

print(trees_product)
