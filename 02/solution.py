file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

bags = [line[line.index(":") + 2:].replace(",", "").split(";") for line in myin]


def part_one():
    ans = 0
    for b, bag in enumerate(bags):
        possible = True
        for group in bag:
            set = group.split(" ")
            for i, s in enumerate(set):
                if s == "red":
                    if int(set[i - 1]) > 12:
                        possible = False
                        break
                if s == "green":
                    if int(set[i - 1]) > 13:
                        possible = False
                        break
                if s == "blue":
                    if int(set[i - 1]) > 14:
                        possible = False
                        break
        if possible:
            ans += b + 1

    print(ans)


def part_two():
    ans = 0
    for bag in bags:
        red, green, blue = (0, 0, 0)
        for group in bag:
            set = group.split(" ")
            for i, s in enumerate(set):
                if s == "red":
                    red = max(red, int(set[i - 1]))
                if s == "green":
                    green = max(green, int(set[i - 1]))
                if s == "blue":
                    blue = max(blue, int(set[i - 1]))
        ans += red * green * blue

    print(ans)


part_one()
part_two()
