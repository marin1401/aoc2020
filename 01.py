#Day 01

with open('./01.txt') as myinput:
    inputlines = myinput.readlines()

entries = [int(i) for i in inputlines]
entries_len = len(entries)

#Part 1

for i in range(entries_len):
    for j in range(i, entries_len):
        if entries[i] + entries[j] == 2020:
            print(entries[i] * entries[j])

#Part 2

for i in range(entries_len):
    for j in range(i, entries_len):
        for k in range(j, entries_len):
            if entries[i] + entries[j] + entries[k] == 2020:
                print(entries[i] * entries[j] * entries[k])
