file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()
from ast import literal_eval
from copy import deepcopy


def parse_list(s):
    return [x for x in literal_eval(s)]


def compare(l, r):
    # print(l, "/", r)

    if type(l) == int and type(r) == int:
        return None if l == r else l < r
    elif type(l) == list and type(r) == list:
        while min(len(l), len(r)) > 0:
            check = compare(l.pop(0), r.pop(0))
            if check is not None:
                return check
            else:
                continue
        return len(l) < len(r) if not len(l) == len(r) else None
    else:
        l = [l] if type(l) == int else l
        r = [r] if type(r) == int else r
        return compare(l, r)


def part_one():
    correct = 0
    i = 0
    while i < len(myin):
        c = compare(parse_list(myin[i]), parse_list(myin[i + 1]))
        correct += ((i // 3) + 1) if c else 0
        # print(myin[i], "/", myin[i + 1], c)
        # print()
        i += 3
    print(correct)


def part_two():
    packets = [parse_list(line) for line in myin if not line == ""]
    packets.extend([[[2]], [[6]]])
    i = 0
    while i < len(packets) - 1:
        swapped = False
        for j in range(len(packets) - i - 1):
            if not compare(deepcopy(packets[j]), deepcopy(packets[j + 1])):
                p = packets[j]
                packets[j] = packets[j + 1]
                packets[j + 1] = p
                swapped = True
        if not swapped:
            break
        else:
            i += 1

    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))


part_one()
part_two()
