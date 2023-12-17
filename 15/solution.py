file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

strings = myin[0].split(",")


def hash_algorithm(string):
    ans = 0
    for char in string:
        ans += ord(char)
        ans *= 17
        ans %= 256
    return (ans)


def part_one():
    print(sum([hash_algorithm(s) for s in strings]))


def part_two():
    boxes = dict.fromkeys(list(range(256)))
    for string in strings:
        key = "".join([x for x in string if x not in "=-" and not x.isdigit()])
        value = "".join([x for x in string if x.isdigit()])
        box = hash_algorithm(key)
        if not boxes[box]:
            boxes[box] = []
        if "=" in string:
            idx = -1
            for i, term in enumerate(boxes[box]):
                if key in term:
                    idx = i
                    break
            if idx != -1:
                boxes[box].pop(idx)
                boxes[box].insert(idx, (key, value))
            else:
                boxes[box].append((key, value))
        elif "-" in string:
            boxes[box] = [x for x in boxes[box] if key not in x]

    ans = 0
    for k in boxes:
        if boxes[k]:
            for i, lenses in enumerate(boxes[k]):
                ans += (k + 1) * (i + 1) * int(lenses[1])
    print(ans)


part_one()
part_two()
