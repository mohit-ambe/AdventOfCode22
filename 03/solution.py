import re

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

# pad the map to prevent edge cases errors
map = [[m for m in "..{}..".format(line)] for line in myin]

# find all numbers in map
numbers = [int(x) for x in re.findall("\d+", "".join(myin))]

R = range(len(map))
C = range(len(map[0]))

# change the numbers in the map to indices, relating to numbers
i = 0
for row in R:
    prev = False
    curr = False
    for col in C:
        if map[row][col].isdigit():
            curr = True
            map[row][col] = str(i)
        else:
            curr = False
            if prev and not curr:
                i += 1
        prev = curr


def part_one():
    adj = []
    for r in R:
        for c in C:
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    if not map[r][c].isdigit() and map[r][c] != ".":
                        try:
                            if map[r + y][c + x].isdigit():
                                adj.append(int(map[r + y][c + x]))
                        except:
                            pass
    print(sum([numbers[a] for a in set(adj)]))


def part_two():
    ans = 0
    for r in R:
        for c in C:
            gear = []
            for y in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    if map[r][c] == "*":
                        try:
                            if map[r + y][c + x].isdigit():
                                gear.append(int(map[r + y][c + x]))
                        except:
                            pass
            gear = [numbers[g] for g in set(gear)]
            if len(gear) == 2:
                ans += gear[0] * gear[1]

    print(ans)


part_one()
part_two()
