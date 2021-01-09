def part_one():
    f = open("input.txt")

    data = []
    lines = 0

    for line in f:
        data.append([])
        for char in line.strip():
            data[lines].append(char)
        lines += 1
    changes = 1
    while changes != 0:
        changes = 0
        new_array = []
        for i in range(len(data)):
            new_array.append([])
            for j in range(len(data[0])):
                if data[i][j] == "L" and count_neighbors(data, i, j) == 0:
                    new_array[i].append("#")
                    changes += 1
                elif data[i][j] == "#" and count_neighbors(data, i, j) >= 4:
                    new_array[i].append("L")
                    changes += 1
                else:
                    new_array[i].append(data[i][j])
        data = new_array
    total_occupied = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "#":
                total_occupied += 1

    return total_occupied



def count_neighbors(seats, row, column):
    occupied_neighbors = 0
    if column + 1 < len(seats[0]) and seats[row][column + 1] == "#":
        occupied_neighbors += 1
    if column - 1 >= 0 and seats[row][column - 1] == "#":
        occupied_neighbors += 1
    if column + 1 < len(seats[0]) and row + 1 < len(seats) and seats[row + 1][column + 1] == "#":
        occupied_neighbors += 1
    if column - 1 >= 0 and row + 1 < len(seats) and seats[row + 1][column - 1] == "#":
        occupied_neighbors += 1
    if row + 1 < len(seats) and seats[row + 1][column] == "#":
        occupied_neighbors += 1
    if column + 1 < len(seats[0]) and row - 1 >= 0 and seats[row - 1][column + 1] == "#":
        occupied_neighbors += 1
    if column - 1 >= 0 and row - 1 >= 0 and seats[row - 1][column - 1] == "#":
        occupied_neighbors += 1
    if row - 1 >= 0 and seats[row - 1][column] == "#":
        occupied_neighbors += 1
    return occupied_neighbors

print(part_one())

def part_two():
    f = open("input.txt")

    data = []
    lines = 0

    for line in f:
        data.append([])
        for char in line.strip():
            data[lines].append(char)
        lines += 1
    changes = 1
    while changes != 0:
        changes = 0
        new_array = []
        for i in range(len(data)):
            new_array.append([])
            for j in range(len(data[0])):
                if data[i][j] == "L" and count_neighbors_part_two(data, i, j) == 0:
                    new_array[i].append("#")
                    changes += 1
                elif data[i][j] == "#" and count_neighbors_part_two(data, i, j) >= 5:
                    new_array[i].append("L")
                    changes += 1
                else:
                    new_array[i].append(data[i][j])
        data = new_array
    total_occupied = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "#":
                total_occupied += 1

    return total_occupied



def count_neighbors_part_two(seats, row, column):
    occupied_neighbors = 0

    i = 0
    j = column + 1
    while True:
        if j < len(seats[0]) and seats[row][j] == "#":
            occupied_neighbors += 1
            break
        elif j >= len(seats[0]) or seats[row][j] == "L":
            break
        j += 1

    i = 0
    j = column - 1
    while True:
        if j >= 0 and seats[row][j] == "#":
            occupied_neighbors += 1
            break
        elif j < 0 or seats[row][j] == "L":
            break
        j -= 1

    i = row + 1
    j = column + 1
    while True:
        if j < len(seats[0]) and i < len(seats) and seats[i][j] == "#":
            occupied_neighbors += 1
            break
        elif j >= len(seats[0]) or i >= len(seats) or seats[i][j] == "L":
            break
        i += 1
        j += 1

    i = row + 1
    j = column - 1
    while True:
        if j >= 0 and i < len(seats) and seats[i][j] == "#":
            occupied_neighbors += 1
            break
        elif j < 0 or i >= len(seats) or seats[i][j] == "L":
            break
        i += 1
        j -= 1

    i = row + 1
    j = 0
    while True:
        if i < len(seats) and seats[i][column] == "#":
            occupied_neighbors += 1
            break
        elif i >= len(seats) or seats[i][column] == "L":
            break
        i += 1

    i = row - 1
    j = column + 1
    while True:
        if j < len(seats[0]) and i >= 0 and seats[i][j] == "#":
            occupied_neighbors += 1
            break
        elif j >= len(seats[0]) or i < 0 or seats[i][j] == "L":
            break
        i -= 1
        j += 1

    i = row - 1
    j = column - 1
    while True:
        if j >= 0 and i >= 0 and seats[i][j] == "#":
            occupied_neighbors += 1
            break
        elif j < 0 or i < 0 or seats[i][j] == "L":
            break
        i -= 1
        j -= 1

    i = row - 1
    j = column
    while True:
        if i >= 0 and seats[i][column] == "#":
            occupied_neighbors += 1
            break
        elif i < 0 or seats[i][column] == "L":
            break
        i -= 1
    return occupied_neighbors

print(part_two())