def part_one():
    f = open("input.txt")

    data = []
    for line in f:
        data.append(int(line.strip()))

    data.sort()
    one_difference = 0
    three_difference = 0
    for i in range(len(data)):
        if i == 0:
            if data[i] == 1:
                one_difference += 1
            elif data[i] == 3:
                three_difference += 1
        if i + 1 < len(data):
            if data[i] + 1 == data[i + 1]:
                one_difference += 1
            elif data[i] + 3 == data[i + 1]:
                three_difference += 1
    three_difference += 1
    return one_difference * three_difference

print(part_one())


def part_two():
    f = open("input.txt")

    data = []
    for line in f:
        data.append(int(line.strip()))
    data.append(0)
    data.sort()
    possibilities = {data[-1]: 1}
    for a in reversed(data[:-1]):
        possibilities[a] = sum(possibilities.get(x, 0) for x in (a + 1, a + 2, a + 3))
    return possibilities[0]

print(part_two())