file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

# myin = [int(x) for x in myin]

def part_one():
    num = ""
    for i in range(len(myin[0])):
        ones = 0
        zeroes = 0
        for line in myin:
            if line[i] == "0":
                zeroes += 1
            else:
                ones += 1
        num += "1" if ones > zeroes else "0"
    antinum = "".join(["1" if l == "0" else "0" for l in num])
    print(int(num, 2) * int(antinum, 2))


def part_two():
    oxy = ""
    carbon = ""

    x = myin.copy()
    for i in range(len(x[0])):
        ones = 0
        zeroes = 0
        for line in x:
            if line[i] == "0":
                zeroes += 1
            else:
                ones += 1
        x = [line for line in x if line[i] == ("1" if ones >= zeroes else "0")]
        if len(x) == 1:
            oxy = x[0]
            break

    x = myin.copy()
    for i in range(len(x[0])):
        ones = 0
        zeroes = 0
        for line in x:
            if line[i] == "0":
                zeroes += 1
            else:
                ones += 1
        x = [line for line in x if line[i] == ("0" if zeroes <= ones else "1")]
        if len(x) == 1:
            carbon = x[0]
            break

    print(int(oxy, 2) * int(carbon, 2))


part_one()
part_two()