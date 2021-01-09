def part_one():
    f = open("input.txt")

    data = []

    for line in f:
        data.append(line.strip())

    start = 0
    cur_index = 25

    while True:
        combo = False
        for i in range(start, cur_index):
            for j in range(start, cur_index):
                if i != j:
                    if int(data[i]) + int(data[j]) == int(data[cur_index]):
                        combo = True
                        break
            if combo:
                break
        if not combo:
            break
        start += 1
        cur_index += 1

    return int(data[cur_index])

def part_two():
    f = open("input.txt")

    data = []
    xmas_number = part_one()
    for line in f:
        data.append(line.strip())

    total = 0
    first_index = 0
    cur_index = 0
    max = int(data[first_index])
    min = int(data[first_index])

    while True:
        if total > xmas_number:
            total = 0
            first_index += 1
            cur_index = first_index
            max = int(data[first_index])
            min = int(data[first_index])
        total += int(data[cur_index])
        if int(data[cur_index]) > max:
            max = int(data[cur_index])
        elif int(data[cur_index]) < min:
            min = int(data[cur_index])
        if total == xmas_number:
            return min + max
        cur_index += 1
        if cur_index >= len(data):
            break

print(part_two())



