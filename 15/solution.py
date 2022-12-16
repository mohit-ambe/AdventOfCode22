file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

s = []
b = []

for line in myin:
    numerics = "".join([l for l in line if l.lower() not in "abcdefghijklmnopqrstuvwxyz ="])
    s.append(tuple([int(x) for x in numerics.split(":")[0].split(",")]))
    b.append(tuple([int(x) for x in numerics.split(":")[1].split(",")]))
    s[-1] = tuple([s[-1][0], s[-1][1], abs(s[-1][0] - b[-1][0]) + abs(s[-1][1] - b[-1][1])])


def impossible_beacons(row, size):
    rx = []
    for x, y, r in s:
        d = r - abs(row - y)
        if d > 0:
            rx.append(tuple([max(min(size, x - d), 0), max(min(size, x + d), 0)]))

    union = []
    for begin, end in sorted(rx):
        if union and union[-1][1] >= begin - 1:
            union[-1][1] = max(union[-1][1], end)
        else:
            union.append([begin, end])

    count = 0
    for u in union:
        count += abs(u[1] - u[0]) + 1
    return count, union


def part_one(row):
    ranges = []
    for x, y, r in s:
        dx = r - abs(row - y)
        if dx > 0:
            ranges.append(tuple([x - dx, x + dx]))

    union = []
    for begin, end in sorted(ranges):
        if union and union[-1][1] >= begin - 1:
            union[-1][1] = max(union[-1][1], end)
        else:
            union.append([begin, end])

    count = 0
    for u in union:
        count += abs(u[1] - u[0]) + 1

    print(count - len([bb for bb in set(b) | set(s) if bb[1] == row]))


def part_two(size):
    impossible = 0;
    possible = []
    i = 0
    for i in range(0, size + 1):
        impossible, possible = impossible_beacons(i, size)
        if impossible <= size:
            break
    span = set(range(0, size + 1))
    for p in possible:
        span = span - set(range(p[0], p[1] + 1))
    print(span.pop() * 4_000_000 + i)


part_one(2_000_000)
part_two(4_000_000)
