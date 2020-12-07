#Day 07

with open('./07.txt') as myinput:
    inputlines = myinput.readlines()

bags = {}
for line in inputlines:
    key, vals = line.split(' bags contain ')
    bags[key] = vals.replace('.\n', '')

bags_which_hold_directly = set()
for key, vals in bags.items():
    if 'shiny gold' in vals:
        bags_which_hold_directly.add(key)

bags_to_check_later = set()

counter = len(bags_which_hold_directly)

def bag_counter(bags, bags_to_check_first, bags_to_check_later, counter):
    for keys, vals in bags.items():
        for bag in bags_to_check_first:
            if bag in vals:
                bags_to_check_later.add(keys)
    counter += len(bags_to_check_later)
    if len(bags_to_check_later) != 0: 
        return bag_counter(bags, bags_to_check_later, set(), counter)
    else:
        return counter

print(bag_counter(bags, bags_which_hold_directly, bags_to_check_later, len(bags_which_hold_directly)))