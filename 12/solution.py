file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
row_length = len(myin[0]) + 2
garden = ["." * row_length]
garden.extend(["." + line + "." for line in myin])
garden.append("." * row_length)


def search(loc, target):
    Q = [loc]
    nodes = {loc}
    visited = set()
    while Q:
        y, x = Q.pop(0)
        if (y, x) in visited or garden[y][x] == '.':
            continue
        visited.add((y, x))

        if garden[y][x] == target:
            nodes.add((y, x))
        for dy, dx in directions:
            if garden[y + dy][x + dx] == target:
                Q.append((y + dy, x + dx))

    return nodes


regions = []
visited = set()
plot = ""
for y, line in enumerate(garden):
    for x, l in enumerate(line):
        if l != plot and l != "." and (y, x) not in visited:
            n = search((y, x), l)
            regions.append(sorted(n))
            visited |= n
        plot = l


def part_one():
    price = 0
    for r in regions:
        area = len(r)
        perimeter = 0
        for y, x in r:
            edges = 4
            for dy, dx in directions:
                if (y + dy, x + dx) in r:
                    edges -= 1
            perimeter += edges
        price += area * perimeter

    print(price)


def part_two():
    price = 0
    for r in regions:
        label = garden[r[0][0]][r[0][1]]
        area = len(r)
        sides = 0
        xlims = [p[1] for p in r]
        ylims = [p[0] for p in r]
        corners = set()
        # search the square in which the region resides
        # for interior and exterior angles
        # the sum of which will be the # of sides
        for y in range(min(ylims), max(ylims) + 1):
            for x in range(min(xlims), max(xlims) + 1):
                angles = ""
                # compare neighbors in all four directions
                # if the current label and the neighbor match,
                # there is no edge there (O)
                for dy, dx in directions:
                    if ((y, x) in r) != ((y + dy, x + dx) in r):
                        angles += "I"
                    else:
                        angles += "O"
                # wrap the edges
                angles += angles[0]
                # two adjacent edges (II) means an angle is present
                right_angles = len([angles[i:i + 2] for i in range(len(angles)) if angles[i:i + 2] == "II"])
                if right_angles:
                    corners.add((y, x))
                sides += right_angles
        # edge case : "mobius strip"
        for c in corners:
            cy, cx = c
            labelling = ""
            for ccy, ccx in [c, (cy, cx + 1), (cy + 1, cx), (cy + 1, cx + 1)]:
                if (ccy, ccx) in corners:
                    labelling += "A" if garden[ccy][ccx] == label else "B"
            if labelling == "ABBA" or labelling == "BAAB":
                sides -= 2
        price += area * sides
    print(price)


part_one()
part_two()
