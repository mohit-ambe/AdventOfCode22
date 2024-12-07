file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

import time

padding = "?"*(len(myin)+2)
map = [[x for x in padding]]
x = 0
y = 0
dir = 0
p1path = set()

for i, line in enumerate(myin):
    map.append([x for x in "?"+line.replace("^", ".")+"?"])
    for j, char in enumerate(line):
        if char == "^":
            y, x = i+1, j+1
map.append([x for x in padding])

def simulate(x=x, y=y, dir=dir, map=map):
    t = time.time()
    dist = set()
    while map[y][x] != "?":
        # if the simulation "times out"
        # it is looping
        if round(time.time() - t, 4) > 0.02:
            return {-1}
        dist.add((y, x))
        if dir == 0:
            if map[y - 1][x] == "#":
                dir = 1
            else:
                y -= 1
        elif dir == 1:
            if map[y][x + 1] == "#":
                dir = 2
            else:
                x += 1
        elif dir == 2:
            if map[y + 1][x] == "#":
                dir = 3
            else:
                y += 1
        else:
            if map[y][x - 1] == "#":
                dir = 0
            else:
                x -= 1
    return dist

def part_one():
    global p1path
    p1path = simulate()
    print(len(p1path))

def part_two():
    looping = 0
    # remove starting position
    for oby,obx in sorted(p1path)[1:]:
        new_map = [line.copy() for line in map.copy()]
        new_map[oby][obx] = "#"
        if simulate(map=new_map) == {-1}:
            looping += 1
    print(looping)


part_one()
part_two()