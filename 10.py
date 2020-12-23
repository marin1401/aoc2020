#Day 10

with open('./10.txt') as myinput:
    inputlines = myinput.readlines()

num_list = sorted([int(line) for line in inputlines])
num_list.insert(0, 0)
num_list.append(num_list[-1] + 3)
num_list_size = len(num_list)

#Part 1

count_diff_1 = 0
count_diff_3 = 0
for i in range(num_list_size - 1):
    diff = num_list[i+1] - num_list[i]
    if diff == 1:
        count_diff_1 += 1
    if diff == 3:
        count_diff_3 += 1

print(count_diff_1 * count_diff_3)

#Part 2

# NOTE:
# For this part I exploited the fact that there aren't more than 5 consecutive adapters
# and that there are always 2 jolts in between consecutive adapter groups

groups = []
group = []
num_check = 0
for num in num_list:
    if num_check + 1 != num:
        if group:
            groups.append(group)
            group = []
    group.append(num)
    num_check = num

arrangements = 1
for group in groups:
    if len(group) == 3:
        arrangements = arrangements * 2
    elif len(group) == 4:
        arrangements = arrangements * 4
    elif len(group) == 5:
        arrangements = arrangements * 7

print(arrangements)
