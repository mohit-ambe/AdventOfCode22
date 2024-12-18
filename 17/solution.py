import re

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

program = [int(x) for x in re.findall("\d+", myin[-1])]


# closed form solution
# 2,4 B = A % 8
# 1,1 B = B ^ 1
# 7,5 C = A // 2**B
# 0,3 A = A // 8
# 4,7 B = B ^ C
# 1,6 B = B ^ 6
# 5,5 B % 8 OUT
# 3,0 repeat

def run_program(a_value, p2):
    out = []
    a = int(re.findall("\d+", myin[0])[0]) if not p2 else a_value
    while a:
        an = (((((a % 8) ^ 1) ^ (a // 2 ** ((a % 8) ^ 1))) ^ 6) % 8)
        out.append(an)
        a //= 8

    return out


def part_one():
    print(",".join([str(x) for x in run_program(0, False)]))


def part_two():
    # brute force each number
    # of the program in reverse

    i = 1
    subset = len(program) - 1
    while subset > -1:
        out = run_program(i, True)
        if out == program[subset:]:
            subset -= 1
            i *= 8
        else:
            i += 1
    print(i // 8)


part_one()
part_two()
