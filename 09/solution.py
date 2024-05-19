file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

myin = [int(x) for x in myin]

invalid = 0


def part_one():
    global invalid

    included = myin[:25]
    for num in myin[25:]:
        if any([x for x in included if num - x in included and x != num - x]):
            included.append(num)
        else:
            invalid = num
            print(num)
            break


def part_two():
    for size in range(2, len(myin)):
        for i in range(len(myin) - size):
            if sum(myin[i:i + size]) == invalid:
                print(min(myin[i:i + size]) + max(myin[i:i + size]))
                return


part_one()
part_two()
