file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def part_one():
    f = []
    i = 0

    for e, l in enumerate(myin[0]):
        if e % 2 == 0:
            f.extend([str(i)] * int(l))
            i += 1
        else:
            f.extend(["."] * int(l))

    checksum = 0
    back_index = [x for x in f[::-1] if x.isdigit()]
    for index, char in enumerate(f[:len(back_index)]):
        if char.isdigit():
            checksum += index * int(char)
        else:
            checksum += index * int(back_index.pop(0))
    print(checksum)


def part_two():
    f = []
    i = 0

    for e, l in enumerate(myin[0]):
        if e % 2 == 0:
            f.append([str(i)] * int(l))
            i += 1
        else:
            f.append(["."] * int(l))

    checksum = 0
    index = 0

    while f:
        block = f.pop(0)
        if "." not in block:
            checksum += sum([i * int(block[0]) for i in range(index, index + len(block))])
        else:
            # while there is space
            while block:
                # find a block small enough
                valid = [x for x in f if len(x) <= len(block) and "".join(x).isdigit()]
                if valid:
                    valid = valid[-1]
                    checksum += sum([i * int(valid[0]) for i in range(index, index + len(valid))])
                    # "move" the block
                    f = f[:f.index(valid)] + [["."] * len(valid)] + f[f.index(valid) + 1:]
                    # remove the claimed space
                    block = block[:len(block) - len(valid)]
                    index += len(valid)
                else:
                    break
        index += len(block)

    print(checksum)


part_one()
part_two()
