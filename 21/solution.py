file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

map = [[*line] for line in myin]
R = range(len(map))
C = range(len(map[0]))

start = tuple()
for r in R:
    for c in C:
        if map[r][c] == "S":
            start = (r, c, 0)


def navigate(steps, p1=False):
    ans = 0
    dist = dict()
    Q = [start]
    seen = set()

    while Q:
        r, c, d = Q.pop(0)
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if d > steps:
            continue
        if p1 and (r not in R or c not in C):
            continue
        if map[r % len(R)][c % len(C)] == "#":
            continue
        if (r, c) in dist.keys():
            dist[(r, c)] = min(dist[(r, c)], d)
        else:
            dist[(r, c)] = d
        for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            Q.append((r + y, c + x, d + 1))

    for k in dist:
        if dist[k] % 2 == steps % 2:
            ans += 1
    return ans


def part_one():
    print(navigate(64, p1=True))


def part_two():
    # using quadratic polynomial
    poly = []
    n = 26501365 // len(myin)
    for i in [0, 1, 2]:
        poly.append(navigate(65 + (131 * i)))
    a = (poly[2] + poly[0] - 2 * poly[1]) // 2
    b = poly[1] - poly[0] - a
    c = poly[0]
    print(a * n * n + b * n + c)


part_one()
part_two()
