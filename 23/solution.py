file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

tree = dict()

for line in myin:
    a, b = line.split("-")
    tree[a] = tree.get(a, []) + [b]
    tree[b] = tree.get(b, []) + [a]


def part_one():
    t_triplets = set()
    for k in [t for t in tree if t.startswith("t")]:
        for i in tree[k]:
            for j in tree[k]:
                if i in tree[j]:
                    t_triplets.add(tuple(sorted([i, j, k])))
    print(len(t_triplets))


def part_two():
    unvisited = list(tree.keys())
    visited = []
    group = []
    groups = dict()
    while unvisited:
        # make a LAN party
        for u in unvisited:
            if all(True if u in tree[key] else False for key in group):
                group.append(u)

        # save the party and only allow
        # new members into the next party
        groups[tuple(sorted(group))] = len(group)
        visited.extend(group)
        group = []
        unvisited = sorted(tree.keys() - visited)

    print([",".join(key) for key, value in groups.items() if value == max(groups.values())][0])


part_one()
part_two()
