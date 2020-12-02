#Day 02

with open('./02.txt') as myinput:
    inputlines = myinput.readlines()

#Part 1
    
min_number_appearance = []
max_number_appearance = []
letter_to_appear = []
password = []

for i in range(len(inputlines)):
    min_number_appearance.append(int(inputlines[i].split()[0].split('-')[0]))
    max_number_appearance.append(int(inputlines[i].split()[0].split('-')[1]))
    letter_to_appear.append(inputlines[i].split()[1][0])
    password.append(inputlines[i].split()[2])

counter = 0
for i in range(len(inputlines)):    
    if min_number_appearance[i] <= password[i].count(letter_to_appear[i]) <= max_number_appearance[i]:
        counter += 1
print(counter)

#Part 2

position_1 = min_number_appearance
position_2 = max_number_appearance
letter_on_position_1 = []
letter_on_position_2 = []

for i in range(len(inputlines)):   
    letter_on_position_1.append(password[i][position_1[i]-1])
    letter_on_position_2.append(password[i][position_2[i]-1])

letters_to_check = [i + j for i, j in zip(letter_on_position_1, letter_on_position_2)]

counter = 0
for i in range(len(inputlines)):
    if letters_to_check[i].count(letter_to_appear[i]) == 1:
        counter += 1
print(counter)