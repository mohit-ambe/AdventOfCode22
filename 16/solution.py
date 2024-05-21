import re

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

valid = []
data = dict()


def part_one():
    total = 0
    for line in myin:
        if not line:
            break
        data[line[:line.index(":")]] = [int(x) for x in re.findall("\d+", line)]

    for ticket in myin[myin.index("nearby tickets:") + 1:]:
        any_invalid = 0
        for num in ticket.split(","):
            num = int(num)
            invalid = 0
            for r in data.values():
                if not (r[0] <= num <= r[1] or r[2] <= num <= r[3]):
                    invalid += 1
            if invalid == len(data):
                total += num
                any_invalid += 1
        if any_invalid == 0:
            valid.append([int(x) for x in ticket.split(",")])
    print(total)


def part_two():
    fields = [list(data.keys()).copy() for i in range(len(valid[0]))]
    total = 1
    mine = myin[myin.index("your ticket:") + 1].split(",")

    for ticket in valid:
        for i, r in enumerate(ticket):
            for key in data:
                if not (data[key][0] <= r <= data[key][1] or data[key][2] <= r <= data[key][3]):
                    try:
                        fields[i].remove(key)
                    except ValueError:
                        pass

    while not all([len(x) == 1 for x in fields]):
        for field in [f[0] for f in fields if len(f) == 1]:
            for i in range(len(fields)):
                if len(fields[i]) == 1:
                    continue
                else:
                    try:
                        fields[i].remove(field)
                    except ValueError:
                        pass

    for i in range(len(fields)):
        if fields[i][0].startswith("departure"):
            total *= int(mine[i])

    print(total)


part_one()
part_two()
