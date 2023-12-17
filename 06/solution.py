import re

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

times, distance = [[int(x) for x in re.findall("\d+", line[line.index(":") + 1:])] for line in myin]


def part_one():
    ans = 1
    for i in range(len(times)):
        wins = 0
        for j in range(times[i]):
            dist = (times[i] - j) * j
            wins += 1 if dist > distance[i] else 0
        ans *= wins
    print(ans)


def part_two():
    ans = 0
    total_time = int("".join([str(_) for _ in times]))
    total_dist = int("".join([str(_) for _ in distance]))
    for j in range(total_time):
        dist = (total_time - j) * j
        ans += 1 if dist > total_dist else 0
    print(ans)


part_one()
part_two()
