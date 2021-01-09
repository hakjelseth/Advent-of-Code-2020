list = []

data = open("input.txt")

for line in data:
    list.append(int(line.strip()))

def find_number(numbers):
    for num1 in numbers:
        for num2 in numbers:
            if num1 + num2 == 2020:
                return num1 * num2


print(find_number(list))

#Part 2

def find_number2(numbers):
    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3

print(find_number2(list))
