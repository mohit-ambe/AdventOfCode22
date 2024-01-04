import re

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

supports = {i: set() for i in range(len(myin))}
supported = {i: set() for i in range(len(myin))}
bricks = [[int(x) for x in re.findall('\d+', line)] for line in myin]


def intersect(x, y):
    return max(x[0], y[0]) <= min(x[3], y[3]) and max(x[1], y[1]) <= min(x[4], y[4])


def above(x, y):
    return min(y[2], y[5]) - max(x[2], x[5]) == 1


bricks.sort(key=lambda b: b[2])

for i, b in enumerate(bricks):
    z = 1
    for check in bricks[:i]:
        if intersect(b, check):
            z = max(z, check[5] + 1)
    b[5] -= b[2] - z
    b[2] = z

bricks.sort(key=lambda b: b[2])

for i in range(len(bricks)):
    if i == 0:
        continue
    for j in range(len(bricks[:i])):
        if intersect(bricks[j], bricks[i]) and above(bricks[j], bricks[i]):
            supports[j].add(i)
            supported[i].add(j)


def part_one():
    safe = 0
    for i in range(len(bricks)):
        if all(len(supported[_]) >= 2 for _ in supports[i]):
            safe += 1
    print(safe)


def part_two():
    chain = 0
    for k in supports:
        Q = [k]
        fell = set()
        stack = {i: list(supported[i]) for i in supported}
        while Q:
            brick = Q.pop(0)
            if brick in fell:
                continue
            fell.add(brick)
            for br in supports[brick]:
                stack[br].remove(brick)
                if not stack[br]:
                    Q.append(br)
        chain += len(fell) - 1
    print(chain)


part_one()
part_two()
