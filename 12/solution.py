from functools import cache

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

springs = []
groups = []

for line in myin:
    springs.append(line.split(" ")[0])
    groups.append(tuple(int(x) for x in line.split(" ")[1].split(",")))


@cache
def solve(spring, group, i=0, gi=0, length=0):
    valid = 0
    if i == len(spring):
        if gi == len(group) - 1 and length == group[gi]:
            return 1
        if gi == len(group) and not length:
            return 1
        else:
            return 0
    for fix in ".#":
        if spring[i] in fix + "?":
            if fix == ".":
                if gi < len(group) and length == group[gi]:
                    valid += solve(spring, group, i + 1, gi + 1, 0)
                elif not length:
                    valid += solve(spring, group, i + 1, gi, 0)
            else:
                valid += solve(spring, group, i + 1, gi, length + 1)
    return valid


def part_one():
    print(sum([solve(springs[i], groups[i]) for i in range(len(myin))]))


def part_two():
    print(sum([solve("?".join([springs[i]] * 5), tuple(x for x in list(groups[i]) * 5)) for i in range(len(myin))]))


part_one()
part_two()
