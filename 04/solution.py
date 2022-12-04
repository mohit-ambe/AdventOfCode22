file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def part_one():
    pairs = 0
    for line in myin:
        one, two = line.split(",")
        onel, oner = one.split("-")
        twol, twor = two.split("-")
        if int(oner) <= int(twor) and int(onel) >= int(twol) or int(twor) <= int(oner) and int(twol) >= int(onel):
            pairs += 1

    print(pairs)


def part_two():
    pairs = 0
    for line in myin:
        one, two = line.split(",")
        ones = set(list(range(int(one.split("-")[0]), int(one.split("-")[1]) + 1)))
        twos = set(list(range(int(two.split("-")[0]), int(two.split("-")[1]) + 1)))
        # print(ones, twos)
        # print(ones & twos)
        pairs += 1 if len(ones & twos) > 0 else 0

    print(pairs)


part_one()
part_two()