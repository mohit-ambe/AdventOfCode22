file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

myin = [line.replace('X', 'A').replace('Y', 'B').replace('Z', 'C') for line in myin]
myin = [line.replace('A', '1').replace('B', '2').replace('C', '3') for line in myin]


def part_one():
    total_score = 0
    wins = ['1 2', '2 3', '3 1']
    ties = ['1 1', '2 2', '3 3']
    total_score += 6 * len([line for line in myin if line in wins])
    total_score += 3 * len([line for line in myin if line in ties])
    total_score += sum([int(line[-1]) for line in myin])

    print(total_score)


def part_two():
    total_score = 0

    # rock, paper, scissor
    # lose, draw, win

    choose = [ [3, 1, 2], [1, 2, 3], [2, 3, 1] ]

    for line in myin:
        total_score += choose[int(line[0]) - 1][int(line[-1]) - 1]
    total_score += 6 * len([line for line in myin if line.endswith('3')])
    total_score += 3 * len([line for line in myin if line.endswith('2')])

    print(total_score)


part_one()
part_two()
