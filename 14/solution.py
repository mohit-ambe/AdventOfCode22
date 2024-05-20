import re
from itertools import product

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def get_floating(n):
    return set([x for x in product(range(2), repeat=n)])


def part_one():
    mem = dict()
    mask = ""
    for line in myin:
        if line.startswith("mask"):
            mask = line.split(" ")[-1]
        else:
            nums = [int(x) for x in re.findall("\d+", line)]
            num = str(bin(nums[1]))[2:]
            num = "0" * (36 - len(num)) + num
            mem[nums[0]] = "".join([num[i] if mask[i] == "X" else mask[i] for i in range(36)])
    print(sum([int(x, 2) for x in mem.values()]))


def part_two():
    mem = dict()
    mask = ""
    for line in myin:
        if line.startswith("mask"):
            mask = line.split(" ")[-1]
        else:
            nums = [int(x) for x in re.findall("\d+", line)]
            num = str(bin(nums[0]))[2:]
            num = "0" * (36 - len(num)) + num
            result = "".join([num[i] if mask[i] == "0" else mask[i] for i in range(36)])
            for perm in get_floating(result.count("X")):
                address = result
                for bit in list(perm):
                    address = address.replace("X", str(bit), 1)
                mem[int(address, 2)] = nums[1]
    print(sum([int(x) for x in mem.values()]))


part_one()
part_two()
