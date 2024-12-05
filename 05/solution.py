file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

rules = {}
updates = []
incorrect = []

for line in myin[:myin.index("")]:
    a, b = tuple([int(x) for x in line.split("|")])
    if a not in rules:
        rules[a] = set()
    rules[a].add(b)

for line in myin[myin.index("") + 1:]:
    updates.append([int(x) for x in line.split(",")])


def part_one():
    total = 0
    for update in updates:
        correct = True
        for i in range(len(update) - 1):
            if update[i] not in rules or update[i + 1] not in rules[update[i]]:
                correct = False
                break
        if correct:
            total += update[len(update) // 2]
        else:
            incorrect.append(update)
    print(total)


def part_two():
    total = 0
    for update in incorrect:
        change = True
        while change:
            change = False
            for i in range(len(update) - 1):
                if update[i] not in rules or update[i + 1] not in rules[update[i]]:
                    temp = update[i]
                    update[i] = update[i + 1]
                    update[i + 1] = temp
                    change = True
        total += update[len(update) // 2]
    print(total)


part_one()
part_two()
