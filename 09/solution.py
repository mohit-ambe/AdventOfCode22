file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

histories = [[int(x) for x in line.split(" ")] for line in myin]


def diff(l, reverse=False):
    diffs = []
    if reverse:
        for i in range(1, len(l)):
            diffs.append(l[i] - l[i - 1])
    else:
        for i in range(len(l) - 1):
            diffs.append(l[i + 1] - l[i])
    return diffs


def extrapolate(p2):
    ans = 0
    for h in histories:
        differences = []
        if p2:
            h.reverse()
        while h.count(0) != len(h):
            differences.append(h)
            h = diff(h)
        ans += sum(d[-1] for d in differences)
    return ans


def part_one():
    print(extrapolate(False))


def part_two():
    print(extrapolate(True))


part_one()
part_two()
