file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

lf = dict()


def init_populate():
    initial = [int(num) for num in myin[0].split(",")]
    for i in range(0, 9):
        lf[i] = 0
    for num in initial:
        lf[num] += 1


def lanternfish():
    repop = int(lf[0])

    for i in range(0, 8):
        lf[i] += lf[i + 1]
        lf[i + 1] = 0

    lf[0] -= repop
    lf[6] += repop
    lf[8] += repop


def part_one():
    init_populate()
    for i in range(80):
        lanternfish()
    print(sum(lf.values()))


def part_two():
    init_populate()
    for i in range(256):
        lanternfish()
    print(sum(lf.values()))


part_one()
part_two()