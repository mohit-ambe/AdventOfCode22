file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()
from sys import getrecursionlimit

instructions = []
for line in myin:
    instructions.append([])
    for tup in line.split(" -> "):
        instructions[-1].append(tuple(tup.split(",")))

obs = []


def create_obs():
    obs.clear()
    for instruction in instructions:
        for i in range(len(instruction) - 1):
            x1, y1 = [int(a) for a in instruction[i]]
            x2, y2 = [int(a) for a in instruction[i + 1]]
            if x2 - x1 == 0 and y2 - y1 != 0:
                for j in range(min(y1, y2), max(y1, y2) + 1):
                    if tuple([x1, j]) not in obs:
                        obs.append(tuple([x1, j]))
            elif x2 - x1 != 0 and y2 - y1 == 0:
                for j in range(min(x1, x2), max(x1, x2) + 1):
                    if tuple([j, y1]) not in obs:
                        obs.append(tuple([j, y1]))


def add_sand(x, y, positions, depth=-1):
    if positions >= getrecursionlimit() - 3:
        return False
    if depth == y:
        obs.append(tuple([x, y - 1]))
        return False
    positions += 1

    if tuple([x, y + 1]) in obs:
        if tuple([x - 1, y + 1]) in obs:
            if tuple([x + 1, y + 1]) in obs:
                obs.append(tuple([x, y]))
                return True
            else:
                return add_sand(x + 1, y + 1, positions, depth)
        else:
            return add_sand(x - 1, y + 1, positions, depth)
    else:
        return add_sand(x, y + 1, positions, depth)


def part_one():
    create_obs()
    rocks = int(len(obs))
    add = True
    while add:
        add = add_sand(500, 0, 1)
    print(len(obs) - rocks)


def part_two():
    create_obs()
    rocks = int(len(obs))

    lowest = float("-inf")
    for t in obs:
        lowest = max(lowest, t[1])
    lowest += 2

    while tuple([500, 0]) not in obs:
        add_sand(500, 0, 1, lowest)
    print(len(obs) - rocks) # 23925

part_one()
part_two()
