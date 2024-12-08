file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

freqs = {}
ylim = len(myin)
xlim = len(myin[0])

for r, line in enumerate(myin):
    for c, l in enumerate(line):
        if l == ".":
            continue
        if l not in freqs:
            freqs[l] = []
        freqs[l].append((r, c))


def create_antinodes(n1, n2):
    x1, y1 = n1
    x2, y2 = n2
    x, y = x2 - x1, y2 - y1
    return {(x1 - x, y1 - y), (x2 + x, y2 + y)}


def create_antinode_line(n1, n2):
    x1, y1 = n1
    x2, y2 = n2
    x, y = x2 - x1, y2 - y1
    nodes = {(x1, y1), (x2, y2)}

    dx, dy = x1, y1
    while 0 <= dx <= xlim and 0 <= dy <= ylim:
        dx -= x
        dy -= y
        nodes.add((dx, dy))

    dx, dy = x2, y2
    while 0 <= dx <= xlim and 0 <= dy <= ylim:
        dx += x
        dy += y
        nodes.add((dx, dy))

    return nodes


def part_one():
    antinodes = set()
    for freq in freqs:
        nodes = freqs[freq]
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                antinodes |= create_antinodes(nodes[i], nodes[j])
    in_map = [(x, y) for x, y in antinodes if 0 <= x < xlim and 0 <= y < ylim]
    print(len(in_map))


def part_two():
    antinodes = set()
    for freq in freqs:
        nodes = freqs[freq]
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                antinodes |= create_antinode_line(nodes[i], nodes[j])
    in_map = [(x, y) for x, y in antinodes if 0 <= x < xlim and 0 <= y < ylim]
    print(len(in_map))


part_one()
part_two()
