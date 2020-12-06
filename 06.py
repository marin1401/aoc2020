#Day 06

all_answers = open('./06.txt').read().split('\n\n')
group_answers = [answers.replace('\n', '') for answers in all_answers]
each_group_answers = [answers.split('\n') for answers in all_answers]

#Part 1

counter = 0
for answers in group_answers:
    counter += len(set(answers))

print(counter)

#Part 2

counter = 0
for answers in each_group_answers:
    answers_set = [set(answer) for answer in answers]
    counter += len(set.intersection(*answers_set))

print(counter)