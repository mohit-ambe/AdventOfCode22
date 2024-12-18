import re

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

directions = [(-1, 0), (-0, 1), (1, -0), (0, -1)]
start = (1, 1)
end = (71, 71)
corrupted = {tuple([int(x) + 1 for x in re.findall("\d+", line)][::-1]) for line in myin[:1024]}
corrupted |= {(0, t) for t in range(73)}
corrupted |= {(72, t) for t in range(73)}
corrupted |= {(t, 0) for t in range(73)}
corrupted |= {(t, 72) for t in range(73)}


def pathfind(space):
    global start, end, directions

    min_dist = dict()
    visited = set()

    min_dist[start] = 0
    Q = [start]

    # Dijkstra's
    while Q:
        Q.sort(key=lambda v: min_dist[v])
        key = Q.pop(0)

        y, x = key

        if key in visited:
            continue
        visited.add(key)

        for dy, dx in set(directions):
            new_key = (y + dy, x + dx)
            if (y + dy, x + dx) not in space:
                if new_key in min_dist:
                    if min_dist[key] + 1 < min_dist[new_key]:
                        min_dist[new_key] = min_dist[key] + 1
                else:
                    min_dist[new_key] = min_dist[key] + 1
                Q.append(new_key)

    if end in min_dist:
        return min_dist[end]
    else:
        return -1


def part_one():
    print(pathfind(corrupted))


def part_two():
    global corrupted

    def next_byte(b):
        return tuple([int(x) + 1 for x in re.findall("\d+", myin[b])][::-1])

    # binary search
    # add bytes in chunks
    # until failure, then fall back
    byte = 1023
    for i in [100, 10, 1]:
        cost = 0
        while cost != -1:
            byte += i
            cost = pathfind(corrupted | {next_byte(b) for b in range(1024, byte)})
        byte -= i

    print(myin[byte])


part_one()
part_two()
