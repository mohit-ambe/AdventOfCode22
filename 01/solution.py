file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

left = [int(line.split("   ")[0]) for line in myin]
right = [int(line.split("   ")[1]) for line in myin]
left.sort()
right.sort()


def part_one():
    print(sum([abs(left[i] - right[i]) for i in range(len(left))]))


def part_two():
    score = 0
    counter = {r: 0 for r in right}

    for r in right:
        counter[r] += 1

    for l in left:
        if l in counter:
            score += l * counter[l]

    print(score)


part_one()
part_two()
