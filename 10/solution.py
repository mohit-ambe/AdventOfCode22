file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def part_one():
    X = 1
    ss = 0
    cycles = 1

    m = []
    for line in myin:
        if line.startswith("addx"):
            m.append("noop")
        m.append(line)

    for line in m:
        cycles += 1
        if line.startswith("addx"):
            X += int(line[line.index(" ") + 1:])

        if (cycles - 20) % 40 == 0:
            ss += cycles * X



    print(ss)


def part_two():
    sprite = list(range(0,3))

    X = 1
    cycles = 1
    drawing = ""

    m = []
    for line in myin:
        if line.startswith("addx"):
            m.append("noop")
        m.append(line)

    for line in m:
        drawing += "#" if ((cycles-1) % 40) in sprite else " "
        cycles += 1
        if line.startswith("addx"):
            X += int(line[line.index(" ") + 1:])
            sprite = list(range(X-1,X+2))

    for i in range(len(drawing)):
        if i % 40 == 0:
            print()
        print(drawing[i], end=" ")


part_one()
part_two()