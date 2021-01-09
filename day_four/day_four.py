def  part_one():
    f = open("input.txt")

    essentials = ["byr","iyr","eyr", "hgt", "hcl", "ecl", "pid"]
    data = f.read().split("\n\n")
    total_valid = 0
    for passport in data:
        total_essentials = 0
        splitted = passport.split()
        for i in splitted:
            if i.split(":")[0] in essentials:
                total_essentials += 1
        if total_essentials == len(essentials):
            total_valid += 1
    return total_valid

print(part_one())

# Part 2

def  part_two():
    f = open("input.txt")

    essentials = ["byr","iyr","eyr", "hgt", "hcl", "ecl", "pid"]
    eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    data = f.read().split("\n\n")
    total_valid = 0
    for passport in data:
        total_essentials = 0
        splitted = passport.split()
        for i in splitted:
            key = i.split(":")[0]
            value = i.split(":")[1]
            if key == "byr" and 1920 <= int(value) <= 2002:
                total_essentials += 1
            elif key == "iyr" and 2010 <= int(value) <= 2020:
                total_essentials += 1
            elif key == "eyr" and 2020 <= int(value) <= 2030:
                total_essentials += 1
            elif key == "hgt":
                if value[len(value)-2:] == "cm" and 150 <= int(value[:len(value)-2]) <= 193:
                    total_essentials += 1
                elif value[len(value)-2:] == "in" and 59 <= int(value[:len(value)-2]) <= 76:
                    total_essentials += 1
            elif key == "hcl":
                bool = True
                if value[0] == "#":
                    for char in value[1:]:
                        if ((char < '0' or char > '9') and (char < 'a' or char > 'f')):
                            bool = False
                            break
                    if bool:
                        total_essentials += 1
            elif key == "ecl":
                if value in eye_color:
                    total_essentials += 1
            elif key == "pid":
                if len(value) == 9:
                    total_essentials += 1

        if total_essentials == len(essentials):
            total_valid += 1
    return total_valid

print(part_two())