file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

row_length = len(myin[0]) + 2
map = ["." * row_length]
map.extend(["." + line + "." for line in myin])
map.append("." * row_length)


def search(r, c, target, diag=True):
    matched = []
    for rr in range(-1, 2):
        if diag:
            if rr == 0:
                continue

        for cc in range(-1, 2):
            if diag:
                if cc == 0:
                    continue
            if rr == cc == 0:
                continue

            if map[r + rr][c + cc] == target:
                matched.append((r + rr, c + cc))
    return matched


def part_one():
    xmas = set()
    Q = []
    for r in range(len(map)):
        for c in range(len(map)):
            if map[r][c] == "X":
                Q.append(((r, c,), (), (), ()))

    visited = []
    while Q:
        x, m, a, s = Q.pop()

        if (x, m, a, s) in visited:
            continue
        visited.append((x, m, a, s))

        if not m:
            for loc in search(x[0], x[1], 'M', diag=False):
                Q.append((x, loc, (), ()))
        elif not a:
            rr, cc = m[0] - x[0], m[1] - x[1]
            if 0 < m[0] + 2 * rr < len(map) and 0 < m[1] + 2 * cc < len(map):
                if map[m[0] + rr][m[1] + cc] == "A" and map[m[0] + 2 * rr][m[1] + 2 * cc] == "S":
                    xmas.add((x, m, (m[0] + rr, m[1] + cc), (m[0] + 2 * rr, m[1] + 2 * cc)))

    print(len(xmas))


def part_two():
    x_mas = 0
    mam_sas = [((-1, 1), (1, -1)), ((-1, -1), (1, 1))]
    centers = []

    for r in range(len(map)):
        for c in range(len(map)):
            if map[r][c] == "A":
                centers.append((r, c))

    for center in centers:
        r, c = center
        m = tuple([(rr - r, cc - c) for rr, cc in search(r, c, "M")])
        s = tuple([(rr - r, cc - c) for rr, cc in search(r, c, "S")])
        if m not in mam_sas and s not in mam_sas and len(m) == len(s) == 2:
            x_mas += 1

    print(x_mas)


part_one()
part_two()
