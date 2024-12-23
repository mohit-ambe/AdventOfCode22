from functools import cache
from itertools import product

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

directions = {(0, -1): "<", (-1, 0): "^", (-0, 1): ">", (1, -0): "v"}
numeric = "789 456 123 .0A".split(" ")
directional = ".^A <v>".split(" ")


def get_sequences(keypad):
    Y = len(keypad)
    X = len(keypad[0])
    seqs = dict()
    for i1 in range(Y):
        for j1 in range(X):
            for i2 in range(Y):
                for j2 in range(X):
                    if keypad[i1][j1] == "." or keypad[i2][j2] == ".":
                        continue
                    if (i1, j1) == (i2, j2):
                        seqs[keypad[i1][j1] + keypad[i2][j2]] = ["A"]
                        continue
                    Q = [(i1, j1, "")]
                    optimal = ["." * 100]
                    while Q:
                        y, x, path = Q.pop(0)

                        if len(path) > min([len(o) for o in optimal]):
                            continue

                        if (y, x) == (i2, j2):
                            if len(path) < min([len(o) for o in optimal]):
                                optimal = [path]
                            else:
                                optimal.append(path)
                            continue
                        for dy, dx in directions:
                            if not 0 <= y + dy < Y or not 0 <= x + dx < X:
                                continue
                            if keypad[y + dy][x + dx] == ".":
                                continue
                            Q.append((y + dy, x + dx, path + directions[(dy, dx)]))
                    seqs[keypad[i1][j1] + keypad[i2][j2]] = [o + "A" for o in optimal]
    return seqs


seq = get_sequences(numeric) | get_sequences(directional)
seq_lens = {k: len(seq[k][0]) for k in seq}


@cache
def seq_length(sequence, iter=25):
    if iter == 1:
        return sum(seq_lens[x + y] for x, y in zip("A" + sequence, sequence))
    length = 0
    for x, y in zip("A" + sequence, sequence):
        length += min(seq_length(subseq, iter - 1) for subseq in seq[x + y])
    return length


def complexify(iter):
    global seq
    complexities = 0
    for code in myin:
        options = [seq[a + b] for a, b in zip("A" + code, code)]
        sequences = ["".join(p) for p in product(*options)]
        complexities += int(code[:-1]) * min([seq_length(s, iter) for s in sequences])
    return complexities


def part_one():
    print(complexify(2))


def part_two():
    print(complexify(25))


part_one()
part_two()
