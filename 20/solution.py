file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

directions = [(-1, 0), (-0, 1), (1, -0), (0, -1)]
start = [(y, line.find("S")) for y, line in enumerate(myin) if line.find("S") != -1][0]
end = [(y, line.find("E")) for y, line in enumerate(myin) if line.find("E") != -1][0]

dist = dict()
Q = [(0, *end)]
visited = set()
while Q:
    d, y, x = Q.pop()
    dist[(y, x)] = d
    if (y, x) in visited:
        continue
    visited.add((y, x))
    for dy, dx in directions:
        if myin[y + dy][x + dx] != "#" and (y + dy, x + dx) not in visited:
            Q.append((d + 1, y + dy, x + dx))


def part_one():
    cheats = dict()
    for d in dist:
        y, x = d
        for dy, dx in directions:
            dd = (y + dy + dy, x + dx + dx)
            if 0 <= dd[0] < len(myin) and 0 <= dd[1] < len(myin[0]):
                if myin[dd[0]][dd[1]] == ".":
                    if (dd, d) not in cheats:
                        cheats[(d, dd)] = abs(dist[d] - dist[dd]) - 2
    print(len([k for k in cheats if cheats[k] >= 100]))


def part_two():
    cheats = dict()
    for d in dist:
        for dd in dist:
            manhattan_dist = abs(d[0] - dd[0]) + abs(d[1] - dd[1])
            if 0 <= manhattan_dist <= 20:
                if 0 <= dd[0] < len(myin) and 0 <= dd[1] < len(myin[0]):
                    if myin[dd[0]][dd[1]] == ".":
                        if (dd, d) not in cheats:
                            cheats[(d, dd)] = abs(dist[d] - dist[dd]) - manhattan_dist
    print(len([k for k in cheats if cheats[k] >= 100]))


part_one()
part_two()
