file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

error = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}

complete = {
    ")":1,
    "]":2,
    "}":3,
    ">":4
}

incomplete = []


def simplify(line):
    while True:
        old = line
        line = line.replace("()", "")
        line = line.replace("[]", "")
        line = line.replace("{}", "")
        line = line.replace("<>", "")
        if len(line) == len(old):
            return line


def part_one():
    score = 0

    for i, line in enumerate(myin):
        line = simplify(line)

        corrupt = False
        for char in line:
            if char not in "([{<":
                corrupt = True
                score += error[char]
                break

        if not corrupt:
            incomplete.append(myin[i])

    print(score)


def part_two():
    scores = []

    for i, line in enumerate(incomplete):
        line = simplify(line)

        line = line.replace("(", ")")
        line = line.replace("[", "]")
        line = line.replace("{", "}")
        line = line.replace("<", ">")
        score = 0
        for char in line[::-1]:
            score *= 5
            score += complete[char]
        scores.append(score)

    scores.sort()
    print(scores[len(scores) // 2])


part_one()
part_two()
