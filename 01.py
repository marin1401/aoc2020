#Day 01

with open('./01.txt') as myinput:
    inputlines = myinput.readlines()

#Part 1

solution = False
for i in inputlines:
    for j in inputlines:
        if int(i)+int(j) == 2020:
            print(int(i)*int(j))
            solution = True
            break
    if solution == True:
        break

#Part 2

solution = False
for i in inputlines:
    for j in inputlines:
        for k in inputlines:
            if int(i)+int(j)+int(k) == 2020:
                print(int(i)*int(j)*int(k))
                solution = True
                break
        if solution == True:
            break
