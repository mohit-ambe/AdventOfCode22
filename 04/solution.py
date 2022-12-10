file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

draw = [int(x) for x in myin[0].split(",")]

boards = [[]]
marked = [[]]
b_i = 0

for line in myin[2:]:
    if line == "":
        b_i += 1
        boards.append([])
        marked.append([])
        continue
    row = [int(x) for x in line.replace("  ", " ").split(" ")]
    boards[b_i].append(row)
    marked[b_i].append([False] * 5)


def check_boards(i):
    for r in marked[i]:
        if r[0] and r[1] and r[2] and r[3] and r[4]:
            return i

    for c in range(len(marked[i][0])):
        col = [line[c] for line in marked[i]]
        if col[0] and col[1] and col[2] and col[3] and col[4]:
            return i

    return -1


def get_board_sum(index):
    unmarked_sum = 0

    for r in range(len(boards[index])):
        for c in range(len(boards[index][r])):
            if not marked[index][r][c]:
                unmarked_sum += boards[index][r][c]

    return unmarked_sum


def part_one():
    for num in draw:
        for b in range(len(boards)):
            for r in range(len(boards[b])):
                for c in range(len(boards[b][r])):
                    if boards[b][r][c] == num:
                        marked[b][r][c] = True
        for i in range(len(boards)):
            index = check_boards(i)
            if index != -1:
                return get_board_sum(index) * num


def part_two():
    won = []
    for num in draw:
        for b in range(len(boards)):
            for r in range(len(boards[b])):
                for c in range(len(boards[b][r])):
                    if boards[b][r][c] == num:
                        marked[b][r][c] = True

        for i in range(len(boards)):
            index = check_boards(i)
            if index != -1 and index not in won:
                won.append(index)
            if len(won) == len(boards):
                return get_board_sum(won[-1]) * num


print(part_one())
print(part_two())
