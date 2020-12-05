#Day 05

with open('./05.txt') as myinput:
    inputlines = myinput.readlines()

seats = [line.strip() for line in inputlines]

def seat_finder(seat, min_value, max_value, direction):
    if seat[0] == direction[0]:
        max_value = (max_value + min_value + 1) // 2 - 1
    elif seat[0] == direction[1]:
        min_value = (max_value + min_value + 1) // 2
    if min_value != max_value:
        return seat_finder(seat[1:], min_value, max_value, direction)
    else:
        return min_value

#Part 1
        
seat_IDs = set()
for seat in seats:
    seat_IDs.add(seat_finder(seat[:-3], 0, 127, 'FB') * 8 + seat_finder(seat[7:], 0, 7, 'LR'))

print(max(seat_IDs))

#Part 2
for missing_ID in range(min(seat_IDs), max(seat_IDs)):
    if missing_ID not in seat_IDs:
        print(missing_ID)