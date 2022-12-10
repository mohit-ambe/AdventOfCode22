file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

coords = dict()


def part_one():
    for line in myin:
        start = [int(x) for x in line.split(" -> ")[0].split(',')]
        end = [int(x) for x in line.split(" -> ")[1].split(',')]

        sx = list(range(start[0], end[0], 1 if start[0] <= end[0] else -1))
        sx.append(end[0])

        sy = list(range(start[1], end[1], 1 if start[1] <= end[1] else -1))
        sy.append(end[1])

        if len(sx) == 1:
            sx = sx * len(sy)
        elif len(sy) == 1:
            sy = sy * len(sx)
        else:
            continue

        for i in range(max(len(sx), len(sy))):
            key = tuple([sx[i], sy[i]])
            if key in coords.keys():
                coords[key] += 1
            else:
                coords.update({key:1})

    print(len([coords[key] for key in coords.keys() if coords[key] > 1]))


def part_two():
    for line in myin:
        start = [int(x) for x in line.split(" -> ")[0].split(',')]
        end = [int(x) for x in line.split(" -> ")[1].split(',')]

        sx = list(range(start[0], end[0], 1 if start[0] <= end[0] else -1))
        sx.append(end[0])

        sy = list(range(start[1], end[1], 1 if start[1] <= end[1] else -1))
        sy.append(end[1])

        if len(sx) == 1:
            sx = sx * len(sy)
        elif len(sy) == 1:
            sy = sy * len(sx)
        # no else continue here

        for i in range(max(len(sx), len(sy))):
            key = tuple([sx[i], sy[i]])
            if key in coords.keys():
                coords[key] += 1
            else:
                coords.update({key:1})

    print(len([coords[key] for key in coords.keys() if coords[key] > 1]))


part_one()
coords = dict()
part_two()