#Day 05

with open('./05.txt') as myinput:
    inputlines = myinput.readlines()

seats = [line.strip() for line in inputlines]

def seat_finder(seat, min_value, max_value, direction):
    value_sum = max_value + min_value
    if seat[0] == direction[0]:
        max_value = value_sum // 2
    elif seat[0] == direction[1]:
        min_value = value_sum // 2 + 1
    if min_value != max_value:
        return seat_finder(seat[1:], min_value, max_value, direction)
    else:
        return min_value

#Part 1
        
seat_IDs = set(seat_finder(seat[:-3], 0, 127, 'FB') * 8 + seat_finder(seat[7:], 0, 7, 'LR') for seat in seats)

print(max(seat_IDs))

#Part 2

print(next(my_seat_ID for my_seat_ID in range(min(seat_IDs), max(seat_IDs)) if my_seat_ID not in seat_IDs))
