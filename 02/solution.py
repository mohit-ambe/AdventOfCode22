file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

interval = []
l = []
p = []

for line in myin:
    line = line.replace("-", " ")
    line = line.replace(":", "")
    interval.append(tuple([int(line.split(" ")[0]), int(line.split(" ")[1])]))
    l.append(line.split(" ")[2])
    p.append(line.split(" ")[3])


def part_one():
    valid = 0
    for i in range(len(myin)):
        if interval[i][0] <= p[i].count(l[i]) <= interval[i][1]:
            valid += 1
    print(valid)


def part_two():
    valid = 0
    for i in range(len(myin)):
        position = p[i][interval[i][0] - 1] + p[i][interval[i][1] - 1]
        if position.count(l[i]) == 1:
            valid += 1
    print(valid)


part_one()
part_two()
