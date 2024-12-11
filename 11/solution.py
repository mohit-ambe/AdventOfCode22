from functools import cache

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

nums = [int(x) for x in myin[0].split()]


@cache
def rules(n):
    if n == 0:
        return (1,)
    elif len(str(n)) % 2 == 0:
        s = str(n)
        return (int(s[:len(s) // 2]), int(s[len(s) // 2:]))
    else:
        return (2024 * n,)


def simulate(iters, numbers):
    stones_dict = {n:0 for n in numbers}
    for n in numbers:
        stones_dict[n] += 1

    for _ in range(iters):
        new_stones = {}
        for stone, count in stones_dict.items():
            if count:
                for new_stone in rules(stone):
                    if new_stone not in new_stones:
                        new_stones[new_stone] = count
                    else:
                        new_stones[new_stone] += count
        stones_dict = new_stones.copy()

    return sum(stones_dict.values())


def part_one():
    print(simulate(25, nums))


def part_two():
    print(simulate(75, nums))


part_one()
part_two()
