from heapq import heappop, heappush

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

f = [[int(x) for x in line] for line in myin]

R = range(len(f))
C = range(len(f[0]))


def pathfind(low, high, p2=False):
    queue = [(-f[0][0], 0, 0, 1, 0, 0), (-f[0][0], 0, 0, 0, 1, 0)]
    seen = set()
    costs = [[1_000_000 for _ in C] for _ in R]
    while queue:
        dist, r, c, x, y, steps = heappop(queue)
        if r not in R or c not in C or (r, c, x, y, steps) in seen:
            continue
        dist += f[r][c]
        if p2 and steps < 4 and r == R.stop - 1 and c == C.stop - 1:
            continue
        costs[r][c] = min(costs[r][c], dist)
        seen.add((r, c, x, y, steps))
        if steps < high:
            heappush(queue, (dist, r + y, c + x, x, y, steps + 1))
        if steps >= low:
            heappush(queue, (dist, r + x, c + y, y, x, 1))
            heappush(queue, (dist, r - x, c - y, -y, -x, 1))
    return costs[-1][-1]


def part_one():
    print(pathfind(0, 3))


def part_two():
    print(pathfind(4, 10, True))


part_one()
part_two()
