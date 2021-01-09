def part_one():
    f = open("input.txt")

    data = f.read().split("\n\n")


    total_answers = 0
    for line in data:
        answers = []
        for char in line.strip():
            if char not in answers:
                answers.append(char)
        if "\n" in answers:
            answers.remove("\n")
        total_answers += len(answers)

    return total_answers

print(part_one())

def part_two():
    f = open("input.txt")

    data = f.read().split("\n\n")


    total_answers = 0
    for line in data:
        answers = {}
        for char in line.strip():
            if char not in answers:
                answers[char] = 1
            else:
                answers[char] = answers.get(char)+1
        if "\n" in answers:
            answers.pop("\n")
        for key in answers:
            if answers.get(key) == len(line.split()):
                total_answers += 1

    return total_answers

print(part_two())
