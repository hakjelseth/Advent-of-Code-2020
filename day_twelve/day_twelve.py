def part_one():
    f = open("input.txt")

    north_south = 0
    east_west = 0

    facing_degree = 90

    for line in f:
        command = line.strip()[0]
        value = int(line.strip()[1:])

        if command == "N":
            north_south += value
        elif command == "S":
            north_south -= value
        elif command == "E":
            east_west += value
        elif command == "W":
            east_west -= value
        elif command == "F":
            if facing_degree == 0:
                north_south += value
            elif facing_degree == 180:
                north_south -= value
            elif facing_degree == 90:
                east_west += value
            elif facing_degree == 270:
                east_west -= value
        elif command == "R":
            facing_degree = (facing_degree + value) % 360
        elif command == "L":
            facing_degree = (facing_degree - value) % 360
    if north_south < 0:
        north_south = north_south*-1
    if east_west < 0:
        east_west = east_west*-1
    print("Manhattan distance: " + str(north_south + east_west))

#part_one()

def part_two():
    f = open("input.txt")

    waypoint_north_south = 1
    waypoint_east_west = 10
    ship_north_south = 0
    ship_east_west = 0

    for line in f:
        print("Ship position: " + str(ship_north_south) + ", " +  str(ship_east_west))
        print("Waypoint position: " + str(waypoint_north_south) + ", " +  str(waypoint_east_west))
        command = line.strip()[0]
        value = int(line.strip()[1:])

        if command == "N":
            waypoint_north_south += value
        elif command == "S":
            waypoint_north_south -= value
        elif command == "E":
            waypoint_east_west += value
        elif command == "W":
            waypoint_east_west -= value
        elif command == "F":
            ship_north_south += waypoint_north_south * value
            ship_east_west += waypoint_east_west * value
        elif command == "R":
            value /= 90
            for i in range(int(value)):
                waypoint_east_west, waypoint_north_south = waypoint_north_south, -waypoint_east_west

        elif command == "L":
            value /= 90
            for i in range(int(value)):
                waypoint_east_west, waypoint_north_south = -waypoint_north_south, waypoint_east_west

    if ship_north_south < 0:
        ship_north_south = ship_north_south * -1
    if ship_east_west < 0:
        ship_east_west = ship_east_west * -1

    print()
    print("FINAL")
    print("Ship position: " + str(ship_north_south) + ", " + str(ship_east_west))
    print("Waypoint position: " + str(waypoint_north_south) + ", " + str(waypoint_east_west))
    print("Manhattan distance: " + str(ship_north_south + ship_east_west))

part_two()