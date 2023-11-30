import time

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

jet = [j for j in myin[0]]
jet_index = 0


def get_rock(i, x, y):
    rocks = [[(x, y), (x + 1, y), (x + 2, y), (x + 3, y)],  # -
             [(x, y + 1), (x + 1, y + 1), (x + 2, y + 1), (x + 1, y), (x + 1, y + 2)],  # +
             [(x, y), (x + 1, y), (x + 2, y), (x + 2, y + 1), (x + 2, y + 2)],  # L
             [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)],  # I
             [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]]  # O
    return rocks[i]


def simulate(rock):
    global jet_index
    x = 2
    y = 4 + max_height
    while True:
        if jet[jet_index] == ">":
            x += collide(get_rock(rock, x + 1, y))
        else:
            x -= collide(get_rock(rock, x - 1, y))

        jet_index = (jet_index + 1) % len(jet)

        next_y = collide(get_rock(rock, x, y - 1))
        y -= next_y
        if next_y == 0:
            break

    chamber.extend(get_rock(rock, x, y))


def collide(rock):
    collision = 1

    if len(list(set(chamber) & set(rock))) > 0:
        collision = 0
    if min(c[0] for c in rock) < 0 or max(c[0] for c in rock) > 6:
        collision = 0
    if min(c[1] for c in rock) < 0:
        collision = 0

    return collision


def part_one():
    global max_height, chamber, jet_index
    max_height = 0
    chamber = [(x, 0) for x in range(7)]
    jet_index = 0

    for i in range(2022):
        chamber = chamber[-100:]
        simulate(i % 5)
        max_height = max(c[1] for c in chamber)
    print(max_height)


def part_two():
    global max_height, chamber, jet_index
    max_height = 0
    chamber = [(x, 0) for x in range(7)]
    jet_index = 0

    cyc_height = 0
    states = {}
    i = 0
    while i < 1000000000000:
        chamber = chamber[-100:]
        simulate(i % 5)
        max_height = max([y for (x, y) in chamber])
        offsets = frozenset([(x, max_height - y) for (x, y) in chamber if max_height - y <= 30])
        this_state = (jet_index, i % 5, offsets)
        if this_state in states and i >= 2022:
            (previ, prevmax_height) = states[this_state]
            dy = max_height - prevmax_height
            di = i - previ
            cycles = (1000000000000 - i) // di
            cyc_height += cycles * dy
            i += cycles * di
        states[this_state] = (i, max_height)
        i += 1
    print(max_height + cyc_height)


part_one()
part_two()
