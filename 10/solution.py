import sys

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

map = [[l for l in line] for line in myin]

R = range(len(map))
C = range(len(map[0]))

start = (0, 0)

path = []


def part_one():
    global start
    for r in R:
        for c in C:
            if map[r][c] == "S":
                start = (r, c)
                if map[r - 1][c] in "|7F" and map[r][c - 1] in "-FL":
                    map[r][c] = "J"
                elif map[r - 1][c] in "|7F" and map[r][c + 1] in "-J7":
                    map[r][c] = "L"
                elif map[r + 1][c] in "|JL" and map[r][c - 1] in "-FL":
                    map[r][c] = "7"
                elif map[r + 1][c] in "|JL" and map[r][c + 1] in "-J7":
                    map[r][c] = "F"
                break

    curr = start
    prev = start
    loop = False
    dist = 0
    while True:
        path.append(curr)
        if loop and curr == start:
            break
        loop = True
        r, c = curr
        if map[r][c] == "|":
            if (r + 1, c) == prev:
                prev = curr
                curr = (r - 1, c)
            else:
                prev = curr
                curr = (r + 1, c)
        elif map[r][c] == "-":
            if (r, c + 1) == prev:
                prev = curr
                curr = (r, c - 1)
            else:
                prev = curr
                curr = (r, c + 1)
        elif map[r][c] == "L":
            if (r - 1, c) == prev:
                prev = curr
                curr = (r, c + 1)
            else:
                prev = curr
                curr = (r - 1, c)
        elif map[r][c] == "J":
            if (r - 1, c) == prev:
                prev = curr
                curr = (r, c - 1)
            else:
                prev = curr
                curr = (r - 1, c)
        elif map[r][c] == "7":
            if (r + 1, c) == prev:
                prev = curr
                curr = (r, c - 1)
            else:
                prev = curr
                curr = (r + 1, c)
        elif map[r][c] == "F":
            if (r + 1, c) == prev:
                prev = curr
                curr = (r, c + 1)
            else:
                prev = curr
                curr = (r + 1, c)
        dist += 1

    print(dist // 2)


def part_two():
    enclosed = 0

    for r in R:
        for c in C:
            if (r, c) not in path:
                map[r][c] = "."

    for r in R:
        for c in C:
            if (r, c) not in path:
                enclosed += len([x for x in range(c) if map[r][x] in "|JL"]) % 2
    print(enclosed)


part_one()
part_two()
