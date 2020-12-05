#Day 05

with open('./05.txt') as myinput:
    inputlines = myinput.readlines()

seats = [line.strip() for line in inputlines]

def row_finder(seat, row_min, row_max):
    if seat[0] == 'F':
        row_max = (row_max + row_min + 1) / 2 - 1
    elif seat[0] == 'B':
        row_min = (row_max + row_min + 1) / 2
    if row_min != row_max:
        row_finder(seat[1:], row_min, row_max)
    else:
        print(row_min)
        return row_min

def column_finder(seat, column_min, column_max):
    if seat[0] == 'L':
        column_max = (column_max + column_min + 1) / 2 - 1
    elif seat[0] == 'R':
        column_min = (column_max + column_min + 1) / 2
    if column_min != column_max:
        column_finder(seat[1:], column_min, column_max)
    else:
        print(column_min)
        return column_min
            
seat = 'BBFFBBFRLL'

print(row_finder(seat[:-3], 0, 127))
print(column_finder(seat[7:], 0, 7))