from functools import cache

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

patterns = myin[0].split(", ")
towels = [line for line in myin[myin.index("") + 1:]]


@cache
def valid(s, p1=True):
    if not p1:
        if len(s) == 0:
            return 1
    else:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return s in patterns
    blocks = [p for p in patterns if s.startswith(p)]
    if p1:
        return any(valid(s[len(b):], p1) for b in blocks)
    else:
        return sum([valid(s[len(b):], p1) for b in blocks])


possible = [t for t in towels if valid(t)]


def part_one():
    print(len(possible))


def part_two():
    print(sum([valid(t, p1=False) for t in possible]))


part_one()
part_two()
