file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part_one():
    sum = 0
    for line in myin:
        one = line[:len(line) // 2]
        two = line[-len(line) // 2:]
        common = set([l for l in one]) & set([l for l in two])
        sum += alphabet.index(list(common)[0])
    print(sum)


def part_two():
    sum = 0
    for i in range(len(myin)):
        if i % 3 != 0:
            continue
        common = set([l for l in myin[i]]) & set([l for l in myin[i + 1]]) & set([l for l in myin[i + 2]])
        sum += alphabet.index(list(common)[0])

    print(sum)


part_one()
part_two()
