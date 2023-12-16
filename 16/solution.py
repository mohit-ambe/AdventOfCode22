file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

tiles = [[*line] for line in myin]

R = range(len(tiles))
C = range(len(tiles[0]))

energized = set()
seen = set()


def navigate(r, c, x, y):
    if (r, c, x, y) in seen:
        return
    if r not in R or c not in C:
        return
    seen.add((r, c, x, y))
    energized.add((r, c))
    if tiles[r][c] == ".":
        while (r + y) in R and (c + x) in C:
            if tiles[r + y][c + x] == ".":
                r += y
                c += x
            else:
                break
            energized.add((r, c))
        return navigate(r + y, c + x, x, y)
    if tiles[r][c] == "/":
        return navigate(r - x, c - y, -y, -x)
    if tiles[r][c] == "\\":
        return navigate(r + x, c + y, y, x)
    if tiles[r][c] == "|":
        if y == 0:
            navigate(r + 1, c, 0, 1)
            navigate(r - 1, c, 0, -1)
            return
        else:
            return navigate(r + y, c + x, x, y)
    if tiles[r][c] == "-":
        if x == 0:
            navigate(r, c + 1, 1, 0)
            navigate(r, c - 1, -1, 0)
            return
        else:
            return navigate(r + y, c + x, x, y)


def maximize(r, c, x, y, me):
    energized.clear()
    seen.clear()
    navigate(r, c, x, y)
    return max(me, len(energized))


def part_one():
    navigate(0, 0, 1, 0)
    print(len(energized))


def part_two():
    max_energy = 0
    for r in R:
        max_energy = maximize(r, 0, 1, 0, max_energy)
        max_energy = maximize(r, len(tiles[0]) - 1, -1, 0, max_energy)
    for c in C:
        max_energy = maximize(0, c, 0, 1, max_energy)
        max_energy = maximize(len(tiles) - 1, c, 0, -1, max_energy)
    print(max_energy)


part_one()
part_two()
