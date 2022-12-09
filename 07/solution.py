file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

dirs = {"/":[]}
sums = dict()


def outer(key):
    possible_outer = [k for k in dirs.keys() if dirs[k].__contains__(key)]
    if len(possible_outer) > 0:
        return possible_outer[0]
    else:
        return "/"


def get_sum(key):
    s = 0
    print(key)
    for num in dirs[key]:
        if type(num) == str:
            s += get_sum(num)
        else:
            s += num
    return s


def part_one():
    i = 1
    key = "/"
    while i < len(myin):
        if myin[i].startswith("$"):
            if myin[i].__contains__("cd"):
                if not myin[i].__contains__(".."):
                    key += "," + myin[i][myin[i].index("cd ") + 3:]
                    if not key in dirs.keys():
                        dirs[key] = []
                    i += 1
                    continue
                else:
                    key = key[::-1]
                    key = key[key.index(",") + 1:]
                    key = key[::-1]
                    i += 1
                    continue
            else:
                j = i + 1
                while j < len(myin) and not myin[j].__contains__("$"):
                    ls_element = myin[j].replace("dir ", "")
                    try:
                        dirs[key].append(int(ls_element[:myin[j].index(" ")]))
                    except ValueError:
                        dirs[key].append(ls_element)
                    j += 1
                i = j

    for k in dirs.keys():
        x = 0
        for file in dirs[k]:
            if type(file) == int:
                x += file
        sums[k] = x

    for k in dirs.keys():
        for j in dirs.keys():
            if k == j:
                continue
            elif j.__contains__(k):
                sums[k] += sums[j]

    print(sum([s for s in sums.values() if s <= 100_000]))

def part_two():
    print(min([v for v in sums.values() if sums["/"] - v < (70_000_000 - 30_000_000)]))


part_one()
part_two()