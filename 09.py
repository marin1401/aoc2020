#Day 09

with open('./09.txt') as myinput:
    inputlines = myinput.readlines()

num_list = [int(line) for line in inputlines]

preamble_len = 25
preamble = [num_list[line] for line in range(preamble_len)]

def get_sums(preamble):
    sums = set()
    for i, num_1 in enumerate(preamble):
        for num_2 in preamble[i:]:
            num_sum = num_1 + num_2
            sums.add(num_sum)
    return sums

def get_encryption_weakness(num_list, black_sheep):
    sub_list = []
    sub_list_sum = 0
    for num in num_list:
        if sub_list_sum != black_sheep:
            sub_list.append(num)
            sub_list_sum += num
        if sub_list_sum == black_sheep:
            return min(sub_list) + max(sub_list)
        if sub_list_sum > black_sheep:
            num_list.pop(0)
            return get_encryption_weakness(num_list, black_sheep)         

#Part 1

for num in range(preamble_len, len(num_list)):
    check_num = num_list[num]
    if check_num in get_sums(preamble):
        preamble.pop(0)
        preamble.append(check_num)
    else:
        black_sheep = check_num
        break

print(black_sheep)

#Part 2

print(get_encryption_weakness(num_list, black_sheep))