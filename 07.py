#Day 07

with open('./07.txt') as myinput:
    inputlines = myinput.readlines()

bags = {}
for line in inputlines:
    bag = ' '.join(line.split()[:2])
    contain = line.split()[4:]
    bags_inside = []
    for i in range(0, len(contain), 4):
        if contain[i].isdigit():
            bags_inside.append((int(contain[i]), ' '.join(contain[i+1:i+3])))
    bags[bag] = bags_inside

#Part 1

def find_bags_which_can_contain():
    for bag, containing_bags in bags.items():
        if bag not in bags_which_can_contain:
            for every_bag in containing_bags:
                if every_bag[1] in bags_which_can_contain:
                    bags_which_can_contain.add(bag)
                    return find_bags_which_can_contain()
    return None

bags_which_can_contain = {'shiny gold'}

find_bags_which_can_contain()

print(len(bags_which_can_contain) - 1)

#Part 2

def count_all_other_bags_inside(the_bag):
    counter = 0
    for bag in bags[the_bag]:
        counter += bag[0] * (1 + count_all_other_bags_inside(bag[1]))
    return counter

print(count_all_other_bags_inside('shiny gold'))
