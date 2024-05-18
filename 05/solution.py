file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

ids = []


def part_one():
    for line in myin:
        rows = list(range(0, 128))
        cols = list(range(0, 8))
        for char in line:
            rm = len(rows) // 2
            cm = len(cols) // 2
            if char == "F":
                rows = rows[:rm]
            elif char == "B":
                rows = rows[rm:]
            elif char == "L":
                cols = cols[:cm]
            elif char == "R":
                cols = cols[cm:]
        ids.append(rows[0] * 8 + cols[0])
    print(max(ids))


def part_two():
    ids.sort()
    prev = ids[0] - 1
    for id in ids:
        if id != prev + 1:
            print(prev + 1)
            break
        else:
            prev = id


part_one()
part_two()
