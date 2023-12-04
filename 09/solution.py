file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

# pad the map with 9s
heightmap = [[9] * (len(myin[0]) + 2)] + [[int(x) for x in "9{}9".format(line)] for line in myin] + [
    [9] * (len(myin[0]) + 2)]

R = range(len(heightmap))
C = range(len(heightmap[0]))
lows = []


def find_basin(r, c, visited):
    if r not in R or c not in C:
        return

    if (r, c) in visited:
        return

    if heightmap[r][c] == 9:
        return

    visited.append((r, c))

    find_basin(r, c + 1, visited)
    find_basin(r, c - 1, visited)
    find_basin(r + 1, c, visited)
    find_basin(r - 1, c, visited)

    return len(visited)


def part_one():
    risk_sum = 0
    for r in R:
        for c in C:
            low = True
            for o in [-1, 1]:
                try:
                    if heightmap[r + o][c] <= heightmap[r][c]:
                        low = False
                except IndexError:
                    pass
                try:
                    if heightmap[r][c + o] <= heightmap[r][c]:
                        low = False
                except IndexError:
                    pass
            if low:
                lows.append((r, c))
                risk_sum += heightmap[r][c] + 1
    print(risk_sum)


def part_two():
    basins = []
    for (r, c) in lows:
        basins.append(find_basin(r, c, []))
    basins.sort(reverse=True)
    print(basins[0] * basins[1] * basins[2])


part_one()
part_two()
