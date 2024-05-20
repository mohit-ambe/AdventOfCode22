file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def inv(a, m):
    m0 = m
    x0 = 0
    x1 = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t

    if x1 < 0:
        x1 = x1 + m0

    return x1


def part_one():
    time = int(myin[0])
    buses = [int(x) for x in myin[1].split(",") if x.isdigit()]
    while True:
        valid = [bus for bus in buses if time % bus == 0]
        if any(valid):
            print((time - int(myin[0])) * valid[0])
            break
        else:
            time += 1


def part_two():
    # chinese remainder thm
    b = [int(x) if x.isdigit() else 1 for x in myin[1].split(",")]
    a = [b[i] - i if b[i] != 1 else 0 for i in range(len(b))]
    a[0] = 0
    cc = 1
    for num in b:
        cc *= num
    c = [cc // b[i] for i in range(len(b))]
    time = 0
    for i in range(len(b)):
        if b[i] != 1:
            time += c[i] * inv(c[i], b[i]) * a[i]
    print(time % cc)


part_one()
part_two()
