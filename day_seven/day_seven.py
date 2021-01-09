class Bag:
    def __init__(self, name, contains):
        self.name = name
        self.contains = contains
    def __str__(self):
        return self.name + " contain " + str(self.contains)


f = open("input.txt")
bags = {}
for line in f:
    words = line.strip().split()
    contain = {}
    i = 4
    while True:
        if words[i] != "no":
            contain[words[i+1] + " " + words[i+2]] = words[i]
        else:
            break
        if words[i+3] == "bags." or words[i+3] == "bag.":
            break
        i += 4
    bag = Bag(words[0] + " " + words[1], contain)
    bags[bag.name] = bag

def search_all(goal_bag):
    counter = 0
    for keys in bags:
        if keys != goal_bag:
            visited = []
            if search(bags.get(keys), goal_bag, visited):
                counter += 1
    return counter

def search(cur_bag, bag, visited):
    visited.append(cur_bag)
    if bag in cur_bag.contains:
        return True
    else:
        for keys in cur_bag.contains:
            if bags.get(keys) not in visited:
                if search(bags.get(keys), bag, visited):
                    return True
        return False

print(search_all("shiny gold"))

#Part two

def amount_of_bags(name):
    cur_bag = bags.get(name)
    counter = 0
    for keys in cur_bag.contains:
        counter += return_bags(bags.get(keys)) * int(cur_bag.contains.get(keys))
    return counter

def return_bags(cur_bag):
    if len(cur_bag.contains) == 0:
        return 1
    counter = 0
    for keys in cur_bag.contains:
        counter += return_bags(bags.get(keys)) * int(cur_bag.contains.get(keys))

    return counter + 1

print(amount_of_bags("shiny gold"))