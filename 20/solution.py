import time

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def decrypt(multiplier=1, iterations=1):
    values = [int(x) * multiplier % (len(myin) - 1) for x in myin]
    file = dict((a, b) for a, b in enumerate(values))
    key_positions = list(file.keys())

    for iter in range(iterations):
        for k in file.keys():
            index = key_positions.index(k)
            key_positions.remove(k)
            if index + file[k] == 0:
                key_positions.insert(len(myin), k)
            elif index + file[k] == len(myin):
                key_positions.insert(1, k)
            else:
                key_positions.insert((index + file[k]) % (len(myin) - 1), k)

    original = [int(x) * multiplier for x in myin]
    decrypt = [original[x] for x in key_positions]
    zero = decrypt.index(0)
    grove = 0

    for num in [1000, 2000, 3000]:
        grove += decrypt[(zero + num) % len(decrypt)]

    return grove


def part_one():
    print(decrypt(1, 1))


def part_two():
    print(decrypt(811589153, 10))


part_one()
part_two()
