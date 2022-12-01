file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def part_one():
    max_cals = float('-inf')
    cals = 0
    for num in myin:
        if num == "":
            if cals > max_cals:
                max_cals = cals
            cals = 0
        else:
            cals += int(num)

    print(max_cals)


def part_two():
    max_cals = [float('-inf'), float('-inf'), float('-inf')]
    cals = 0
    for num in myin:
        if num == "":
            if cals > max_cals[0]:
                max_cals[0] = cals
                max_cals.sort()
            cals = 0
        else:
            cals += int(num)

    print(sum(max_cals))


part_one()
part_two()
