file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def part_one():
    x = y = r = 0
    for line in myin:
        d, k = line[0], int(line[1:])
        if d == "R":
            r += k
        if d == "L":
            r -= k
        r %= 360
        if d == "F":
            if r == 0:
                d = "E"
            elif r == 90:
                d = "S"
            elif r == 180:
                d = "W"
            elif r == 270:
                d = "N"
        if d == "N":
            y += k
        if d == "S":
            y -= k
        if d == "E":
            x += k
        if d == "W":
            x -= k
    print(abs(x) + abs(y))


def part_two():
    x = y = r = 0
    wx = 10
    wy = 1
    for line in myin:
        d, k = line[0], int(line[1:])
        if d == "N":
            wy += k
        if d == "S":
            wy -= k
        if d == "E":
            wx += k
        if d == "W":
            wx -= k
        if d == "F":
            x += k * wx
            y += k * wy
        if d == "L":
            for _ in range(k // 90):
                wx, wy = -wy, wx
        if d == "R":
            for _ in range(k // 90):
                wx, wy = wy, -wx
    print(abs(x) + abs(y))


part_one()
part_two()
