file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

eqs = [[int(x) for x in line.replace(":","").split(" ")] for line in myin]


def solve(result, Q, p2=False):
    new = Q.pop(0)
    if len(Q) != 0:
        if p2:
            return (solve(result + new, Q.copy(), p2)
                    or solve(result * new, Q.copy(), p2)
                    or solve(int(str(result) + str(new)), Q.copy(), p2))
        else:
            return (solve(result + new, Q.copy(), p2)
                    or solve(result * new, Q.copy(), p2))
    else:
        return (result == new)


def part_one():
    solvable = 0
    for eq in [x.copy() for x in eqs]:
        eq.append(eq[0])
        eq = eq[1:]
        if solve(eq[0], eq[1:]):
            solvable += eq[-1]
    print(solvable)


def part_two():
    solvable = 0
    for eq in [x.copy() for x in eqs]:
        eq.append(eq[0])
        eq = eq[1:]
        if solve(eq[0], eq[1:], p2=True):
            solvable += eq[-1]
    print(solvable)


part_one()
part_two()
