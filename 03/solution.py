file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

R = len(myin)
C = len(myin[0])

map = [[*line] for line in myin]


def slide(down, right):
    trees = 0
    r = c = 0
    while r < R - 1:
        r += down
        c = (c + right) % C
        if map[r][c] == "#":
            trees += 1
    return trees


def part_one():
    print(slide(1, 3))


def part_two():
    print(slide(1, 1) *
          slide(1, 3) *
          slide(1, 5) *
          slide(1, 7) *
          slide(2, 1))


part_one()
part_two()
