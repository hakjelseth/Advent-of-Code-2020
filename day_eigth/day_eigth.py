def part_one():
    f = open("input.txt")

    array = []
    visited = []
    acc = 0
    cur_index = 0
    for line in f:
        array.append(line.strip())

    while True:
        if cur_index in visited:
            break
        elif cur_index >= len(array):
            break
        visited.append(cur_index)
        command = array[cur_index].split()[0]
        value = array[cur_index].split()[1]
        if command == "acc":
            acc += int(value)
            cur_index += 1
        elif command == "jmp":
            cur_index += int(value)
        else:
            cur_index += 1

    return acc


def part_two():
    f = open("input.txt")

    array = []
    visited = []
    acc = 0
    cur_index = 0
    brute  = False
    for line in f:
        array.append(line.strip())

    while True:
        if cur_index in visited:
            break
        elif cur_index >= len(array):
            break
        visited.append(cur_index)
        command = array[cur_index].split()[0]
        value = array[cur_index].split()[1]
        if command == "acc":
            acc += int(value)
            cur_index += 1
        elif command == "jmp":
            if brute == False and brute_force(array.copy(), visited.copy(), acc, cur_index+1):
                cur_index += 1
                brute = True
            else:
                cur_index += int(value)
        else:
            if brute == False and brute_force(array.copy(), visited.copy(), acc, cur_index + int(value)):
                cur_index += int(value)
                brute = True
            else:
                cur_index += 1

    return acc

def brute_force(array, visited, acc, cur_index):
    while True:
        if cur_index in visited:
            return False
        elif cur_index >= len(array):
            return True
        visited.append(cur_index)
        command = array[cur_index].split()[0]
        value = array[cur_index].split()[1]
        if command == "acc":
            acc += int(value)
            cur_index += 1
        elif command == "jmp":
            cur_index += int(value)
        else:
            cur_index += 1


print(part_two())