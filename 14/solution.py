from functools import cache

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

dish = [[*line] for line in myin]

R = range(1, len(dish))
C = range(len(dish[0]))


def roll(map):
    ans = 0
    for c in C:
        change = True
        while change:
            change = False
            for r in R:
                if map[r][c] == "O" and map[r - 1][c] == ".":
                    map[r - 1][c] = "O"
                    map[r][c] = "."
                    change = True

    for r in range(len(map)):
        for c in C:
            if map[r][c] == "O":
                ans += len(map) - r
    return ans


def rotate(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp


def part_one():
    print(roll(dish))


def part_two():
    global dish
    platform = dish.copy()
    # cheat code
    for cyc in range(1000):
        for rotation in "NWSE":
            roll(platform)
            rotate(platform)
    ans = 0
    for r in range(len(platform)):
        for c in range(len(platform[0])):
            if platform[r][c] == "O":
                ans += len(platform) - r
    print(ans)


part_one()
part_two()
