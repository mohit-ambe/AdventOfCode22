file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

pins = [map.split("\n") for map in "\n".join(myin).split("\n\n")]

locks = []
keys = []
for p in pins:
    h = [line.count("#") - 1 for line in ["".join(row) for row in zip(*p)]]
    if "#" not in p[0]:
        keys.append(h)
    else:
        locks.append(h)

intersecting = 0
for locks in locks:
    for key in keys:
        if all([locks[i] + key[i] <= 5 for i in range(5)]):
            intersecting += 1
print(intersecting)
