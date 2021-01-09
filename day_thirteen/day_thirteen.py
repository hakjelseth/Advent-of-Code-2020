import re
from math import gcd

def part_one():
    f = open("input.txt").read()

    timestamp = int(f.split()[0])

    bus_ids = re.findall('\d+', f.split()[1])
    bus_ids = [ int(x) for x in bus_ids ]


    temp = bus_ids[0]

    while True:
        if temp >= timestamp:
            min_timestamp = temp
            min_id = bus_ids[0]
            break
        temp += bus_ids[0]

    for bus_id in bus_ids:
        temp = bus_id
        while True:
            if temp >= timestamp:
                min_timestamp = temp
                min_id = bus_id
                break
            temp += bus_id

    return (min_timestamp-timestamp) * min_id


def part_two():
    f = open("input.txt").read()


    bus_ids = f.split()[1].split(",")
    timestamp = 0

    matched_buses = [int(bus_ids[0])]

    while True:
        timestamp += compute_lcm(matched_buses)
        for i, bus in enumerate(bus_ids):
            if bus != 'x':
                if (timestamp + i) % int(bus) == 0:
                    if int(bus) not in matched_buses:
                        matched_buses.append(int(bus))
        if len(matched_buses) == len(bus_ids) - bus_ids.count('x'):
            break
    print(timestamp)

def compute_lcm(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm
part_two()