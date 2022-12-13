file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()
from collections import deque

heights = [[l for l in line] for line in myin]
elevations = dict(
    zip([l for l in "abcdefghijklmnopqrstuvwxyz"], list(range(1, 27))))
elevations.update({"S":1, "E":26})


def pathfinder(start, end):
    elevs = deque()
    elevs.append((start, 0))
    visited = set()
    finished = []
    while len(elevs) > 0:
        curr = elevs.popleft()
        visited.add(curr[0])
        if curr[0] == end:
            finished.append(curr[1])
            continue
        for mod in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            y = curr[0][0] + mod[0]
            x = curr[0][1] + mod[1]
            if (y, x) in visited or x < 0 or y < 0:
                continue
            try:
                if elevations[heights[y][x]] <= elevations[heights[curr[0][0]][curr[0][1]]] + 1:
                    elevs.append(tuple([(y, x), curr[1] + 1]))
                    visited.add((y, x))
            except IndexError:
                pass

    return finished


def part_one():
    start = tuple([[myin.index(line), line.find("S")] for line in myin
                   if not line.find("S") == -1][0])
    end = tuple([[myin.index(line), line.find("E")] for line in myin
                 if not line.find("E") == -1][0])
g
    print(min(pathfinder(start, end)))


def part_two():
    end = tuple([[myin.index(line), line.find("E")] for line in myin
                 if not line.find("E") == -1][0])
    paths = []
    for i in range(len(heights)):
        for j in range(len(heights[i])):
            if heights[i][j] == "a":
                paths.extend(pathfinder(tuple([i, j]), end))
    print(min(paths))


part_one()
part_two()
