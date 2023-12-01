file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

cubes = {tuple([int(x) for x in line.split(",")]) for line in myin}


def surface_area(cubelist):
    sa = 0
    for cube in cubelist:
        x, y, z = cube
        neigbors = {(x + 1, y, z), (x - 1, y, z), (x, y + 1, z),
                    (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)}
        sa += 6
        for n in neigbors:
            if n in cubelist:
                sa -= 1
    return sa


def part_one():
    print(surface_area(cubes))


def part_two():
    flooded = {(0, 0, 0)}
    low = min([min(cube) for cube in list(cubes)]) - 1
    high = max([max(cube) for cube in list(cubes)]) + 1
    changed = True
    while changed:
        changed = False
        for x in range(low, high + 1):
            for y in range(low, high + 1):
                for z in range(low, high + 1):
                    neigbors = {(x + 1, y, z), (x - 1, y, z), (x, y + 1, z),
                                (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)}
                    if (x, y, z) in cubes or (x, y, z) in flooded:
                        continue
                    if low in (x, y, z) or high in (x, y, z):
                        changed = True
                        flooded.update({(x, y, z)})
                    for n in neigbors:
                        if n in flooded:
                            changed = True
                            flooded.update({(x, y, z)})
    outside_area = high - low + 1
    outside_area *= outside_area * 6
    print(surface_area(flooded) - outside_area)


part_one()
part_two()
