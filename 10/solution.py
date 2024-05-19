from functools import cache

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

myin = [int(x) for x in myin]
myin.append(max(myin) + 3)
myin.append(0)
myin.sort()


def part_one():
    diffs = []
    for i in range(len(myin) - 1):
        diffs.append(myin[i + 1] - myin[i])

    print(len([x for x in diffs if x == 1]) * len([x for x in diffs if x == 3]))


@cache
def path(start, end):
    ans = 0
    if start == end:
        return 1
    for n in range(start + 1, start + 4):
        if n in myin:
            ans += path(n, end)
    return ans


def part_two():
    print(path(0, max(myin)))


part_one()
part_two()
