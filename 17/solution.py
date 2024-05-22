from itertools import product

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def part_one():
    active = []
    for y, line in enumerate(myin):
        for x, l in enumerate(line):
            if l == "#":
                active.append((y, x, 0))

    for cycle in range(6):
        new_active = []
        ranges = [range(min([d[i] for d in active]) - 1, max([d[i] for d in active]) + 2) for i in
                  range(len(active[0]))]
        for x, y, z in product(*ranges):
            adj = 0
            for dx, dy, dz in product([-1, 0, 1], repeat=3):
                if dx == dy == dz == 0:
                    continue
                if (x + dx, y + dy, z + dz) in active:
                    adj += 1
            if (x, y, z) not in active and adj == 3:
                new_active.append((x, y, z))
            elif (x, y, z) in active and adj in [2, 3]:
                new_active.append((x, y, z))

        active = [_ for _ in new_active]
    print(len(active))


def part_two():
    active = []
    for y, line in enumerate(myin):
        for x, l in enumerate(line):
            if l == "#":
                active.append((y, x, 0, 0))

    for cycle in range(6):
        new_active = []
        ranges = [range(min([d[i] for d in active]) - 1, max([d[i] for d in active]) + 2) for i in
                  range(len(active[0]))]
        for x, y, z, w in product(*ranges):
            adj = 0
            for dx, dy, dz, dw in product([-1, 0, 1], repeat=4):
                if dx == dy == dz == dw == 0:
                    continue
                if (x + dx, y + dy, z + dz, w + dw) in active:
                    adj += 1
            if (x, y, z, w) not in active and adj == 3:
                new_active.append((x, y, z, w))
            elif (x, y, z, w) in active and adj in [2, 3]:
                new_active.append((x, y, z, w))

        active = [_ for _ in new_active]
    print(len(active))


part_one()
part_two()
