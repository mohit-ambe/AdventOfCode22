file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def sim(lines):
    acc = 0
    index = 0
    visited = []

    while index not in visited:
        if index >= len(lines):
            return acc, True
        visited.append(index)
        a, b = lines[index].split(" ")
        b = int(b)
        if a == "jmp":
            index += b
            continue
        elif a == "acc":
            acc += b
        index += 1

    return acc, False


def part_one():
    print(sim(myin)[0])


def part_two():
    for i in range(len(myin)):
        lines = myin.copy()
        if lines[i].startswith("jmp"):
            lines[i] = lines[i].replace("jmp", "nop")
        elif lines[i].startswith("nop"):
            lines[i] = lines[i].replace("nop", "jmp")
        acc, term = sim(lines)
        if term:
            print(acc)


part_one()
part_two()
