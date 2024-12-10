file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
row_length = len(myin[0]) + 2
slopes = ["." * row_length]
slopes.extend(["." + line + "." for line in myin])
slopes.append("." * row_length)

trailheads = []
for r, line in enumerate(slopes):
    for c, l in enumerate(line):
        if l == "0":
            trailheads.append((r, c, 0))


def part_one():
    score = []
    for t in trailheads:
        subscore = 0
        Q = [t]
        visited = set()
        while Q:
            y, x, val = Q.pop(0)
            if (y, x, val) in visited:
                continue
            visited.add((y, x, val))
            if val == 9:
                subscore += 1
                continue
            for dy, dx in directions:
                s = slopes[y + dy][x + dx]
                if s.isdigit() and int(s) - 1 == val:
                    Q.append((y + dy, x + dx, val + 1))
        score.append(subscore)
    print(sum(score))


def part_two():
    score = []
    for t in trailheads:
        subscore = 0
        Q = [t]
        while Q:
            y, x, val = Q.pop(0)
            if val == 9:
                subscore += 1
                continue
            for dy, dx in directions:
                s = slopes[y + dy][x + dx]
                if s.isdigit() and int(s) - 1 == val:
                    Q.append((y + dy, x + dx, val + 1))
        score.append(subscore)
    print(sum(score))


part_one()
part_two()
