from itertools import combinations

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

map = [[l for l in line] for line in myin]

R = range(len(map))
C = range(len(map[0]))

rblank = [row for row in R if "#" not in "".join(map[row])]
cblank = [col for col in C if "#" not in "".join([m[col] for m in map])]


def expand_galaxy(expander):
    galaxies = []
    lengths = 0
    for r in R:
        for c in C:
            if map[r][c] == "#":
                rex = len([rr for rr in rblank if rr in range(r)]) * (expander - 1)
                cex = len([cc for cc in cblank if cc in range(c)]) * (expander - 1)
                galaxies.append((r + rex, c + cex))

    for c in combinations(range(len(galaxies)), 2):
        g, gg = c
        lengths += abs(galaxies[gg][0] - galaxies[g][0]) + abs(galaxies[gg][1] - galaxies[g][1])
    return lengths


def part_one():
    print(expand_galaxy(2))


def part_two():
    print(expand_galaxy(1_000_000))


part_one()
part_two()
