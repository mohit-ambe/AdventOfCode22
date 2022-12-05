file = open("input.txt", "r")
myin = [line.strip("\n") for line in file.readlines()]
file.close()

nums = myin.index('') - 1


def make_crates():
    x = []
    for num in myin[nums][1:].split("   "):
        c = []
        for i in range(nums - 1, -1, -1):
            try:
                c.append(myin[i][myin[nums].index(num)])
            except IndexError:
                break
        x.append([a for a in c if not a == " "])
    return x


def part_one():
    instructions = myin[nums + 2:]
    for step in instructions:
        origin = int(step[step.index("from ") + 5:step.index(" to")])
        destination = int(step[step.index("to ") + 3:])
        move = int(step[5:step.index(" from ")])

        toMove = crates[origin - 1][-move:]
        crates[origin - 1] = crates[origin - 1][:-move]
        crates[destination - 1].extend(toMove[::-1])

    print(''.join([crate[-1] for crate in crates]))


def part_two():
    instructions = myin[nums + 2:]
    for step in instructions:
        origin = int(step[step.index("from ") + 5:step.index(" to")])
        destination = int(step[step.index("to ") + 3:])
        move = int(step[5:step.index(" from ")])

        toMove = crates[origin - 1][-move:]
        crates[origin - 1] = crates[origin - 1][:-move]
        crates[destination - 1].extend(toMove)  # no [::-1] here so crates don't reverse

    print(''.join([crate[-1] for crate in crates]))


crates = make_crates()
part_one()
crates = make_crates()
part_two()
