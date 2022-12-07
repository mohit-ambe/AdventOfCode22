file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

myin = [int(x) for x in myin]


def part_one():
    inc = 0
    for i in range(1, len(myin)):
        if myin[i] > myin[i - 1]:
            inc += 1
    print(inc)


def part_two():
    inc = 0
    for i in range(1, len(myin)):
        if sum(myin[i-3:i]) > sum(myin[i-4:i-1]):
            inc += 1
    print(inc)


part_one()
part_two()
