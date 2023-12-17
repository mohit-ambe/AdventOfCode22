from math import lcm

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

directions = [*myin[0]]

network = {}
for line in myin[2:]:
    val = tuple(line[line.index("(") + 1:-1].split(", "))
    network[line[:line.index(" =")]] = val


def travel(key, p2=False):
    steps = 0
    i = 0
    while (not p2 and key != "ZZZ") or (p2 and not key.endswith("Z")):
        if directions[i % len(directions)] == "R":
            key = network[key][1]
        else:
            key = network[key][0]
        i += 1
        steps += 1
    return steps


def part_one():
    print(travel("AAA"))


def part_two():
    print(lcm(*[travel(k, True) for k in network.keys() if k.endswith("A")]))


part_one()
part_two()
