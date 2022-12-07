file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def part_one():
    pos = [0,0]
    for line in myin:
        step = line[:line.index(" ")]
        num = int(line[line.index(" ") + 1:])
        if step == 'forward':
            pos[0] += num
        elif step == 'up':
            pos[1] -= num
        else:
            pos[1] += num
    print(pos[0] * pos[1])


def part_two():
    pos = [0, 0, 0]
    for line in myin:
        step = line[:line.index(" ")]
        num = int(line[line.index(" ") + 1:])
        if step == 'forward':
            pos[0] += num
            pos[2] += num * pos[1]
        elif step == 'up':
            pos[1] -= num
        else:
            pos[1] += num
    print(pos[0] * pos[2])


part_one()
part_two()
