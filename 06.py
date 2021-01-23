#Day 06

with open('./06.txt') as myinput:
    inputlines = myinput.read()

groups_answers = [answers.split('\n') for answers in inputlines.split('\n\n')]

#Part 1

print(sum(len(set(''.join(group_answers))) for group_answers in groups_answers))

#Part 2

print(sum(len(set.intersection(*(set(each_person_answers) for each_person_answers in group_answers))) for group_answers in groups_answers))
