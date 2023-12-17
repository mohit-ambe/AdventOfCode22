file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

maps = []
map = []
for line in myin:
    if line:
        map.append(line)
    else:
        maps.append(map.copy())
        map.clear()
maps.append(map.copy())
map.clear()


def reflect(pattern, multiplier, p2=False):
    for axis in range(1, len(pattern)):
        errors = 0
        for r in range(axis):
            if axis + (axis - r) - 1 in range(len(pattern)):
                if pattern[r] != pattern[axis + (axis - r) - 1]:
                    for err in range(len(pattern[r])):
                        if pattern[r][err] != pattern[axis + (axis - r) - 1][err]:
                            errors += 1
        if (not p2 and errors == 0) or (p2 and errors == 1):
            return axis * multiplier
    return 0


def part_one():
    ans = 0
    for m in maps:
        ans += reflect(m.copy(), 100)
        transpose = [list(row) for row in zip(*m.copy())]
        ans += reflect(transpose.copy(), 1)
    print(ans)


def part_two():
    ans = 0
    for m in maps:
        ans += reflect(m.copy(), 100, True)
        transpose = [list(row) for row in zip(*m.copy())]
        ans += reflect(transpose.copy(), 1, True)
    print(ans)


part_one()
part_two()
