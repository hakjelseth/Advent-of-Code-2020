import re
def part_one():
    f = open("input.txt")

    memory = {}
    mask = ""
    for line in f:
        if line.split()[0] == "mask":
            mask = line.split()[2].strip()
        else:
            addr = "{:036b}".format(int(line.split()[2].strip()))
            val = ""
            for m, v in zip(mask, addr):
                if m == "X":
                    val += v
                else:
                    val += m
            memory[line.split()[0]] = int(val, 2)

    return sum(memory.values())

print(part_one())

def get_addr(addr_mask):
    if "X" in addr_mask:
        for r in ("0", "1"):
            for addr in get_addr(addr_mask.replace("X", r, 1)):
                yield addr
    else:
        yield addr_mask

def part_two():
    f = open("input.txt")

    mask = None
    mem = {}
    for line in f:
        lh, rh = line.split(" = ")
        if lh == "mask":
            mask = rh
        if lh.startswith("mem"):
            addr = re.match("^mem\[(\d+)\]", lh).groups()[0]
            addr = "{:036b}".format(int(addr))
            argv = int(rh)

            addr_m = ""
            for m, v in zip(mask, addr):
                if m == "0":
                    addr_m += v
                else:
                    addr_m += m

            for addr in get_addr(addr_m):
                mem[int(addr, 2)] = argv

    return sum(mem.values())

print(part_two())