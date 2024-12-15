import re

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

nums = [[int(x) for x in re.findall("-?\d+", line)] for line in myin]

LENGTH, WIDTH, YDIV, XDIV = 101, 103, 50, 51


def mod(v, n1, n2):
    return complex(int(v.real % n1), int(v.imag % n2))


def part_one():
    quads = [[0, 0], [0, 0]]
    for px, py, vx, vy in nums:
        p = complex(px, py)
        v = complex(vx, vy)
        for i in range(100):
            p = mod(p + v, LENGTH, WIDTH)
        if p.real != YDIV and p.imag != XDIV:
            y, x = int(p.imag // XDIV), int(p.real // YDIV)
            quads[1 if y else 0][1 if x else 0] += 1
    print(quads[0][0] * quads[0][1] * quads[1][0] * quads[1][1])


def part_two():
    global nums

    # let the loop run
    # with ans = 10000
    # and watch :/
    ans = 8159

    for i in range(ans):
        grid = []
        for _ in range(WIDTH):
            grid.append([])
            for _ in range(LENGTH):
                grid[-1].append(".")
        original = len(nums)
        for px, py, vx, vy in nums.copy():
            p = complex(px, py)
            v = complex(vx, vy)
            p = mod(p + v, LENGTH, WIDTH)
            grid[int(p.imag)][int(p.real)] = "#"
            nums.append([p.real, p.imag, vx, vy])
        nums = nums[-original:]
    # for line in grid:
    #     print("".join(line))
    print(ans)


part_one()
part_two()
