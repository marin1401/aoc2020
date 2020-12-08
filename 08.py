#Day 08

with open('./08.txt') as myinput:
    inputlines = myinput.readlines()

operation = []
argument = []
for line in inputlines:
    operation.append(line.split()[0])
    argument.append(int(line.split()[1]))

accumulator = 0
i = 0
been_there_done_that = set()
while i < len(inputlines):
    if i in been_there_done_that:
        break
    if operation[i] == 'nop':
        been_there_done_that.add(i)
        i += 1
    if operation[i] == 'acc':
        been_there_done_that.add(i)
        accumulator += argument[i]
        i += 1
    if operation[i] == 'jmp':
        been_there_done_that.add(i)
        i += argument[i]

#Part 1

print(accumulator)