file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()
from copy import deepcopy

monkeys = []

i = 0
while i < len(myin):
    monkeys.append([])
    monkeys[-1].append([int(x) for x in myin[i + 1][myin[i + 1].index(":") + 2:].split(", ")])
    monkeys[-1].append(myin[i + 2][myin[i + 2].index("old "):])
    for j in [3, 4, 5]:
        monkeys[-1].append(int(myin[i + j][myin[i + j].index("y ") + 2:]))
    i += 7


def part_one():
    monk = deepcopy(monkeys)
    inspections = [0] * len(monk)
    for r in range(20):
        for m in monk:
            inspections[monk.index(m)] += len(m[0])
            while len(m[0]) > 0:
                m[0][0] = eval(m[1].replace("old", str(m[0][0]))) // 3
                if m[0][0] % m[2] == 0:
                    monk[m[3]][0].append(m[0][0])
                else:
                    monk[m[4]][0].append(m[0][0])
                m[0].pop(0)
    inspections.sort()
    print(inspections)
    print(inspections[-1] * inspections[-2])


def part_two():
    monk = deepcopy(monkeys)
    inspections = [0] * len(monk)
    mods = [x[2] for x in monk]
    lcm = 1
    for m in mods:
        lcm *= m
    for r in range(10000):
        for m in monk:
            inspections[monk.index(m)] += len(m[0])
            while len(m[0]) > 0:
                m[0][0] = eval(m[1].replace("old", str(m[0][0])))
                m[0][0] %= lcm
                if m[0][0] % m[2] == 0:
                    monk[m[3]][0].append(m[0][0])
                else:
                    monk[m[4]][0].append(m[0][0])
                m[0].pop(0)
    inspections.sort()
    print(inspections[-1] * inspections[-2])


part_one()
part_two()
