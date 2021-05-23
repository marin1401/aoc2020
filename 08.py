#Day 08

with open('./08.txt') as myinput:
    inputlines = myinput.readlines()

operation, argument = [], []
for line in inputlines:
    operation.append(line.split()[0])
    argument.append(int(line.split()[1]))

def get_acc1():
    been_there_done_that = set()
    accumulator, i = 0, 0
    while i < len(operation):
        if i in been_there_done_that:
            break
        if operation[i] == 'nop':
            been_there_done_that.add(i)
            i += 1
        if operation[i] == 'acc':
            been_there_done_that.add(i)
            accumulator += argument[i]
            i += 1
            if len(operation) - 1 <= i:
                break
        if operation[i] == 'jmp':
            been_there_done_that.add(i)
            i += argument[i]
    return accumulator, i

#Part 1

print(get_acc1()[0])

#Part 2

ops = (('jmp', 'nop'), ('nop', 'jmp'))

def get_acc2():
    for ins in ops:
        for op in range(len(operation)):
            if operation[op] == ins[0]:
                operation[op] = ins[1]
                sol = get_acc1()
                if sol[1] == len(operation) - 1:
                    return sol[0]
                operation[op] = ins[0]

print(get_acc2())
