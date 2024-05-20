file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

R = len(myin)
C = len(myin[0])

map = [[*line] for line in myin]


def sim(p1, seats):
    global map
    change = True
    while change:
        new_map = []
        change = False
        for y, line in enumerate(map):
            new_map.append([])
            for x, l in enumerate(line):
                if l == ".":
                    new_map[y].append(l)
                    continue
                occ = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dy == dx == 0:
                            continue
                        try:
                            i = 1
                            while True:
                                if y + dy * i in range(R) and x + dx * i in range(C):
                                    if map[y + dy * i][x + dx * i] == "#":
                                        occ += 1
                                        break
                                    elif not p1 and map[y + dy * i][x + dx * i] == "L":
                                        break
                                else:
                                    if not p1:
                                        break
                                if p1:
                                    break
                                i += 1
                        except IndexError:
                            pass
                if l == "L" and occ == 0:
                    new_map[y].append("#")
                    change = True
                elif l == "#" and occ >= seats:
                    new_map[y].append("L")
                    change = True
                else:
                    new_map[y].append(l)
        map = [x.copy() for x in new_map.copy()]
    return len([mm for m in map for mm in m if mm == "#"])


def part_one():
    print(sim(True, 4))


def part_two():
    print(sim(False, 5))


part_one()
map = [[*line] for line in myin]
part_two()
