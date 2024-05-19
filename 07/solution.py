file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def part_one():
    lines = myin.copy()
    Q = ['shiny gold']
    colors = set()

    while Q:
        color = Q.pop(0)
        colors.add(color)
        containing = [line for line in lines if color in line and not line.startswith(color)]
        for c in containing:
            Q.append(c[:c.find(" bag")])
    print(len(colors) - 1)


def count_bag(line):
    total = 0
    line = line.replace(" no ", " 0 ")[:-1]
    line = line.replace(" bags", "")
    line = line.replace(" bag", "")

    for bag in line[line.find("contain ") + 8:].split(", "):
        num = int("".join([x for x in bag if x.isdigit()]))
        color = "".join([x for x in bag if not x.isdigit()]).strip()
        if color == "other":
            continue
        total += num + num * count_bag([line for line in myin if line.startswith(color)][0])

    return total


def part_two():
    print(count_bag([line for line in myin if line.startswith("shiny gold")][0]))


part_one()
part_two()
