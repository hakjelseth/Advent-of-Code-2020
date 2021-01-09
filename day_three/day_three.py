f = open("input.txt")
row = 0
array = []
for line in f:
    array.append([])
    for char in line.strip():
        array[row].append(char)
    row += 1

height = len(array)
width = len(array[0])

y = 1
x = 3

trees = 0
while y < height:
    if array[y][x] == "#":
        trees += 1
    y += 1
    x = (x+3) % (width)

#print(trees)

# Part 2

def find_num_of_trees(down, right):
    trees = 0
    y = down
    x = right
    while y < height:
        if array[y][x] == "#":
            trees += 1
        y += down
        x = (x+right) % (width)
    return trees

num1 = int(find_num_of_trees(1, 1))
num2 = int(find_num_of_trees(1, 3))
num3 = int(find_num_of_trees(1, 5))
num4 = int(find_num_of_trees(1, 7))
num5 = int(find_num_of_trees(2, 1))

print(num1 * num2 * num3 * num4 * num5)
