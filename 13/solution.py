import re

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

games = []
g = []
for line in myin:
    if line:
        g.extend([int(x) for x in re.findall("\d+", line)])
    else:
        games.append(g)
        g = []
games.append(g)


def det(m):
    # [[m0, m1]]
    # [[m2, m3]]
    return m[0] * m[3] - m[1] * m[2]


def compute(games):
    tokens = 0
    for game in games:
        # Cramer's Rule
        # 2 Var Sys Eq
        a0 = det([game[0], game[2], game[1], game[3]])
        a1 = det([game[4], game[2], game[5], game[3]])
        a2 = det([game[0], game[4], game[1], game[5]])
        if a0:
            if a1 / a0 == a1 // a0 and a2 / a0 == a2 // a0:
                tokens += 3 * (a1 / a0) + (a2 / a0)
    return int(tokens)


def part_one():
    print(compute(games))


def part_two():
    unit = 10_000_000_000_000
    games_converted = [[g[i] if i < 4 else g[i] + unit for i in range(6)] for g in games]
    print(compute(games_converted))


part_one()
part_two()
