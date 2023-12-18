file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def dig_trench(plan):
    ans = 0
    r = 0
    c = 0
    peri = 0
    trench = [(0, 0)]
    for p in plan:
        d, m, = p
        if d in "R0":
            c += m
        if d in "D1":
            r += m
        if d in "L2":
            c -= m
        if d in "U3":
            r -= m
        peri += m
        trench.append((r, c))

    # shoelace
    for (x1, y1), (x2, y2) in zip(trench[:-1], trench[1:]):
        ans += (x2 - x1) * (y1 + y2)
    return ans // 2 + peri // 2 + 1  # pick's thm


def part_one():
    plan = [(line.split(" ")[0], int(line.split(" ")[1])) for line in myin]
    print(dig_trench(plan))


def part_two():
    plan = []
    for line in myin:
        plan.append((line.split(" ")[-1][-2], int(line.split(" ")[-1][2:-2], base=16)))
    print(dig_trench(plan))


part_one()
part_two()
