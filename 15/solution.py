file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

directions = {"^": (-1, 0), ">": (-0, 1), "v": (1, -0), "<": (0, -1)}
instructions = "".join(myin[myin.index("") + 1:])


def find_blocks(y, x, dy, dx, map, p2=False):
    push = set()
    if dy == 0 or not p2:
        i = 1
        # check blocks
        while map[y + i * dy][x + i * dx] in "O[]":
            push.add((y + i * dy, x + i * dx))
            i += 1
        # check edge
        if map[y + i * dy][x + i * dx] == "#":
            return set(), y, x
        else:
            return push, y + dy, x + dx
    else:
        # check blocks
        Q = [(y + dy, x + dx)]
        visited = set()
        while Q:
            Q.sort()
            by, bx = Q.pop(0)
            if (by, bx) in visited:
                continue
            visited.add((by, bx))
            if 0 <= by <= len(map) and 0 <= bx <= len(map[0]) and map[by][bx] in "[]":
                push.add((by, bx))
                Q.append((by + dy, bx + dx))
                if map[by][bx] == "[":
                    Q.append((by, bx + 1))
                if map[by][bx] == "]":
                    Q.append((by, bx - 1))
        # check edges
        check_edges = {(py + dy, px + dx) for py, px in push if (py + dy, px + dx) not in push}
        for ey, ex in check_edges:
            if 0 <= ey <= len(map) and 0 <= ex <= len(map[0]) and map[ey][ex] in "#":
                return set(), y, x
        return push, y + dy, x + dx


def part_one():
    y, x = 0, 0
    map = [[l for l in line] for line in myin[:myin.index("")]]
    for i in range(len(map)):
        if "@" in map[i]:
            y, x = i, map[i].index("@")
            map[y][x] = "."
            break

    for inst in instructions:
        dy, dx = directions[inst]
        if map[y + dy][x + dx] == "#":
            continue
        elif map[y + dy][x + dx] == "O":
            push, y, x = find_blocks(y, x, dy, dx, map)
            for py, px in push:
                map[py][px] = "."
            for py, px in push:
                map[py + dy][px + dx] = "O"
        else:
            y += dy
            x += dx

    coords = 0
    for my, line in enumerate(map):
        for mx, char in enumerate(line):
            if char == "O":
                coords += 100 * my + mx
    print(coords)


def part_two():
    y, x = 0, 0
    map = [[l for l in line] for line in myin[:myin.index("")]]
    for i, line in enumerate(map):
        line = "".join(line)
        line = line.replace("#", "##")
        line = line.replace("O", "[]")
        line = line.replace(".", "..")
        line = line.replace("@", "@.")
        map[i] = [*line]

    for i in range(len(map)):
        if "@" in map[i]:
            y, x = i, map[i].index("@")
            map[y][x] = "."
            break

    for inst in instructions:
        dy, dx = directions[inst]
        if map[y + dy][x + dx] == "#":
            pass
        elif map[y + dy][x + dx] in "[]":
            push, y, x = find_blocks(y, x, dy, dx, map, p2=True)
            for py, px in push:
                map[py][px] = "."
            for py, px in push:
                map[py + dy][px + dx] = "O"
            for i, line in enumerate(map):
                map[i] = [*"".join(line).replace("OO", "[]")]
        else:
            y += dy
            x += dx
        # print(f"Move {inst}:")
        # for i, line in enumerate(map):
        #     if i == y:
        #         ch = "".join(line)
        #         ch = ch[:x] + "@" + ch[x + 1:]
        #         print(ch)
        #     else:
        #         print("".join(line))  # print()

    coords = 0
    for my, line in enumerate(map):
        for mx, char in enumerate(line):
            if char == "[":
                coords += 100 * my + mx
    print(coords)


part_one()
part_two()
