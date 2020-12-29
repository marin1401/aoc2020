#Day 2

with open('./02.txt') as myinput:
    inputlines = myinput.readlines()

inputlines = [i.split() for i in inputlines]

policy_1_counter, policy_2_counter = 0, 0
for line in inputlines:
    num_1, num_2 = map(int, line[0].split('-'))
    if num_1 <= line[2].count(line[1][0]) <= num_2:
        policy_1_counter += 1
    if (line[2][num_1-1] == line[1][0]) != (line[2][num_2-1] == line[1][0]):
        policy_2_counter += 1

#Part 1

print(policy_1_counter)

#Part 2

print(policy_2_counter)
