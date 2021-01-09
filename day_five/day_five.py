import math

def part_one():
    f = open("input.txt")
    data = []

    for line in f:
        data.append(line.strip())
    max_seat_id = 0

    for boarding_pass in data:
        row_low = 0
        row_high = 127
        collumn_low = 0
        collumn_high = 7

        for char in boarding_pass:
            if char == "F":
                row_high = row_high - 1  - math.floor((row_high-row_low)/2)

            elif char == "B":
                row_low = row_low + math.ceil((row_high-row_low)/2)

            elif  char == "L":
                collumn_high = collumn_high - 1 - math.floor((collumn_high - collumn_low) / 2)

            elif char == "R":
                collumn_low = collumn_low + math.ceil((collumn_high-collumn_low)/2)


        seat_id = row_low * 8  + collumn_low
        if seat_id > max_seat_id:
            max_seat_id =  seat_id
    return max_seat_id

print(part_one())

def part_two():
    f = open("input.txt")
    data = []
    seat_ids = []

    for line in f:
        data.append(line.strip())

    for boarding_pass in data:
        row_low = 0
        row_high = 127
        collumn_low = 0
        collumn_high = 7

        for char in boarding_pass:
            if char == "F":
                row_high = row_high - 1  - math.floor((row_high-row_low)/2)

            elif char == "B":
                row_low = row_low + math.ceil((row_high-row_low)/2)

            elif  char == "L":
                collumn_high = collumn_high - 1 - math.floor((collumn_high - collumn_low) / 2)

            elif char == "R":
                collumn_low = collumn_low + math.ceil((collumn_high-collumn_low)/2)


        seat_id = row_low * 8  + collumn_low
        seat_ids.append(seat_id)

    seat_ids.sort()
    for i in range(len(seat_ids)):
        if seat_ids[i] + 2 == seat_ids[i+1]:
            return seat_ids[i] + 1
    return 0

print(part_two())