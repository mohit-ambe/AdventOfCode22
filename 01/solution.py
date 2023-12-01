file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def part_one():
    t = 0
    for line in myin:
        s = ""
        for l in line:
            if l.isnumeric():
                s += l
        t += int(s[0] + s[-1])
    print(t)


def part_two():
    t = 0
    for line in myin:
        for i, s in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            line = line.replace(s, s[0] + str(i + 1) + s[-1])
        s = ""
        for l in line:
            if l.isnumeric():
                s += l
        t += int(s[0] + s[-1])
    print(t)


part_one()
part_two()
