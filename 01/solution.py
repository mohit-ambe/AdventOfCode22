file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

myin = [int(x) for x in myin]


def part_one():
    entries = list(set([x for x in myin if 2020 - x in myin]))
    print(entries[0] * entries[1])


def part_two():
    entries = list(set([y for y in myin for x in myin if 2020 - x - y in myin]))
    print(entries[0] * entries[1] * entries[2])


part_one()
part_two()
