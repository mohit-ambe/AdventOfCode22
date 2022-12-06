file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def find_key(key_length):
    for i in range(key_length - 1, len(myin[0]) - key_length):
        if len(set([b for b in myin[0][i:i + key_length]])) == key_length:
            return i + key_length


def part_one():
    print(find_key(4))


def part_two():
    print(find_key(14))


part_one()
part_two()
