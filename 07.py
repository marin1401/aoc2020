#Day 07

with open('./07.txt') as myinput:
    inputlines = myinput.readlines()

bags = {}
new_bags = {}
for line in inputlines:
    key, vals = line.split(' bags contain ')
    bags[key] = vals.replace('\n', '').replace(' bags', '').replace(' bag', '').replace('no other', '').replace('.', '')

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

#Part 2

# NOTE:
# Had a lot of trouble getting this part to work.
# Did a recursion with the dict above, but couldn't get counter to add properly.
# For an easy recursive solution, dict needs to be written in a different way:

new_bags_dict = {}
for keys, vals in bags.items():
    vals_list = [line for line in vals.split(', ')]
    bags = [' '.join(line.split()[-2:]) for line in vals_list]
    num = [line[0] for line in vals_list if len(line) != 0]
    new_bags_dict[keys] = [(int(num[i]), bags[i]) for i in range(len(bags)) if len(num) != 0]

def yo_dawg(the_bag):
    counter = 0
    for bag in new_bags_dict[the_bag]:
        counter += bag[0] * (1 + yo_dawg(bag[1]))
    return counter

print(yo_dawg('shiny gold'))
