f = open("input.txt")

num_of_valid = 0

for line in f:
    splitted = line.split()
    numbers = splitted[0].split("-")
    letter = splitted[1][0]
    password = splitted[2]
    num_of_letter = 0
    for char in password:
        if char == letter:
            num_of_letter += 1

    if int(numbers[0]) <= num_of_letter <= int(numbers[1]):
        num_of_valid += 1

print(num_of_valid)


#Part 2

f = open("input.txt")

num_of_valid = 0

for line in f:
    splitted = line.split()
    numbers = splitted[0].split("-")
    letter = splitted[1][0]
    password = splitted[2]
    if int(numbers[0]) < len(password) >= int(numbers[1]):
        if (password[int(numbers[0])-1] == letter) != (password[int(numbers[1])-1] == letter):
            num_of_valid += 1


print(num_of_valid)