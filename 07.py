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

def bag_counter(bags, bags_to_check_first, bags_to_check_later, checked_bags):
    for keys, vals in bags.items():
        for bag in bags_to_check_first:
            if bag in vals:
                bags_to_check_later.add(keys)
    checked_bags.update(bags_to_check_first)
    if len(bags_to_check_later) != 0: 
        return bag_counter(bags, bags_to_check_later, set(), checked_bags)
    else:
        return len(checked_bags)

#Part 1
        
print(bag_counter(bags, bags_which_hold_directly, set(), set()))
