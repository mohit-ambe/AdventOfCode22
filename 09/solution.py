file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def follow(t, h):
    x = h[1] - t[1]
    y = h[0] - t[0]

    if abs(x) < 2 and abs(y) < 2:
        return t
    elif abs(x) == 2 and y == 0:
        t[1] += x//abs(x)
    elif abs(y) == 2 and x == 0:
        t[0] += y // abs(y)
    else:
        t[1] += x // abs(x)
        t[0] += y // abs(y)

    return t


def part_one():
    T = [4, 0]
    H = [4, 0]
    pos = []

    for line in myin:
        for i in range(int(line[line.index(" ") + 1:])):

            if line[0] == "L":
                H[1] -= 1
            elif line[0] == "R":
                H[1] += 1

            if line[0] == "U":
                H[0] -= 1
            elif line[0] == "D":
                H[0] += 1

            T = follow(T, H)
            pos.append(str(T[0]) + "," + str(T[1]))

    print(len(set(pos)))


def part_two():
    T1 = [4, 0]
    T2 = [4, 0]
    T3 = [4, 0]
    T4 = [4, 0]
    T5 = [4, 0]
    T6 = [4, 0]
    T7 = [4, 0]
    T8 = [4, 0]
    T9 = [4, 0]
    H = [4, 0]
    pos = []

    for line in myin:
        for i in range(int(line[line.index(" ") + 1:])):

            if line[0] == "L":
                H[1] -= 1
            elif line[0] == "R":
                H[1] += 1

            if line[0] == "U":
                H[0] -= 1
            elif line[0] == "D":
                H[0] += 1

            T1 = follow(T1, H)
            T2 = follow(T2, T1)
            T3 = follow(T3, T2)
            T4 = follow(T4, T3)
            T5 = follow(T5, T4)
            T6 = follow(T6, T5)
            T7 = follow(T7, T6)
            T8 = follow(T8, T7)
            T9 = follow(T9, T8)

            pos.append(str(T9[0]) + "," + str(T9[1]))
    print(len(set(pos)))


part_one()
part_two()