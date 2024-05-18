file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def part_one():
    total = 0
    letters = []
    for line in myin:
        if line:
            letters.extend([*line])
        else:
            total += len(set(letters))
            letters.clear()
    total += len(set(letters))
    print(total)


def part_two():
    total = 0
    people = 0
    letters = ""
    for line in myin:
        if line:
            people += 1
            letters += line
        else:
            all_yes = [letter for letter in {*letters} if letters.count(letter) == people]
            total += len(all_yes)
            people = 0
            letters = ""
    all_yes = [letter for letter in {*letters} if letters.count(letter) == people]
    total += len(all_yes)
    print(total)


part_one()
part_two()
