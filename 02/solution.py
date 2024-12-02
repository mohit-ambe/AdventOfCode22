file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

nums = [[int(x) for x in line.split()] for line in myin]
safe = []


def is_safe(line):
    if line == sorted(line) or line == sorted(line)[::-1]:
        diffs = [abs(line[i] - line[i - 1]) for i in range(1, len(line))]
        if 0 < min(diffs) and max(diffs) < 4:
            return True


for i, line in enumerate(nums):
    if is_safe(line):
        safe.append(i)


def part_one():
    print(len(safe))


def part_two():
    also_safe = 0
    for n, line in enumerate(nums):
        if n in safe:
            continue

        for j in range(len(line)):
            new_line = line[:j] + line[j + 1:]
            if is_safe(new_line):
                also_safe += 1
                break

    print(len(safe) + also_safe)


part_one()
part_two()
