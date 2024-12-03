import re

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def part_one():
    count = 0

    for line in myin:
        for mul in re.findall(r"mul\(\d+,\d+\)", line):
            numerics = [int(x) for x in re.findall(r"\d+", mul)]
            count += numerics[0] * numerics[1]

    print(count)


def part_two():
    count = 0
    do = True

    for line in myin:
        for op in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line):
            if op == "do()":
                do = True
            if op == "don't()":
                do = False

            if do and "mul" in op:
                numerics = [int(x) for x in re.findall(r"\d+", op)]
                count += numerics[0] * numerics[1]

    print(count)


part_one()
part_two()
