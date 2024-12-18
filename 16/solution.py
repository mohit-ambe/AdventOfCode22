file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

directions = [(-1, 0), (-0, 1), (1, -0), (0, -1)]

start = (len(myin) - 2, myin[-2].find("S"))
end = (1, myin[1].find("E"))
ey, ex = end

forks = {(0, 0)}


def pathfind(maze=None):
    global start, end, directions
    if maze is None:
        maze = myin

    min_dist = dict()
    visited = set()

    min_dist[(start[0], start[1], start[0], start[1] - 1)] = 0
    Q = [(start[0], start[1], start[0], start[1] - 1)]
    # Dijkstra's
    while Q:
        Q.sort(key=lambda v: min_dist[v])
        key = Q.pop(0)

        y, x, py, px = key

        if key in visited:
            continue
        visited.add(key)

        prev_dir = (y - py, x - px)
        rev_dir = (py - y, px - x)
        for dy, dx in set(directions) - {rev_dir}:
            new_key = (y + dy, x + dx, y, x)
            if maze[y + dy][x + dx] != "#":
                score = 1 if (dy, dx) == prev_dir else 1001
                if new_key in min_dist:
                    if min_dist[key] + score < min_dist[new_key]:
                        min_dist[new_key] = min_dist[key] + score
                else:
                    min_dist[new_key] = min_dist[key] + score
                Q.append(new_key)
    best_costs = sorted([(min_dist[k], k) for k in min_dist if (k[0], k[1]) == end])
    if best_costs:
        optimal, dest = best_costs[0]
    else:
        return -1, []
    path = [dest]
    while (start[0], start[1], start[0], start[1] - 1) not in path:
        neighbors = [k for k in min_dist if (k[0], k[1]) == (path[-1][2], path[-1][3])]
        for n in neighbors:
            if min_dist[path[-1]] - min_dist[n] in [1, 1001]:
                path.append(n)
    return optimal, [(p[0], p[1]) for p in path]


def part_one():
    global forks
    cost, path = pathfind()
    print(cost)
    for my, mx in path:
        if myin[my][mx] == ".":
            neighbors = set()
            for mdy, mdx in directions:
                if myin[my + mdy][mx + mdx] == ".":
                    neighbors.add((my + mdy, mx + mdx))
            if len(neighbors) >= 3:
                forks |= neighbors


def part_two():
    maze = [[*line] for line in myin]
    optimal, path = pathfind(maze=maze)
    tiles = set(path)

    # for all forks on
    # the path taken in part 1,
    # add a border on each side and
    # do part 1 again on this new map
    # if alternate routes are found,
    # append their paths to tiles
    for i, (fy, fx) in enumerate([f for f in forks if f in path.copy()]):
        maze_copy = [m.copy() for m in maze].copy()
        maze_copy[fy][fx] = "#"
        cost, path = pathfind(maze=maze_copy)
        if cost == optimal and path[0] == end:
            tiles |= set(path)
    print(len(tiles))


part_one()
part_two()
