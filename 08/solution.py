file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()
from itertools import permutations


def part_one():
    count = 0
    for line in myin:
        for digit in line[line.index("|") + 1:].split():
            if len(digit) in [2, 3, 4, 7]:
                count += 1
    print(count)


def part_two():
    count = 0
    segment_configs = ["012456", "26", "02345", "02346", "1236", "01346", "013456", "026", "0123456", "012346"]
    for l in myin:
        num = 0
        perms = [''.join(p) for p in permutations('abcdgef')]
        for p in perms:
            # t0 tl1 tr2 m3 b4 bl5 br6
            dc = dict(zip(p, list(range(7))))
            go_next = False
            for d in l[:l.index(" |")].split(" "):
                d = [dc[letter] for letter in d]
                d.sort()
                if "".join([str(s) for s in d]) not in segment_configs:
                    go_next = True
                    break
            if go_next:
                continue
            else:
                for d in l[l.index("|") + 2:].split(" "):
                    d = [dc[letter] for letter in d]
                    d.sort()
                    num *= 10
                    num += segment_configs.index("".join([str(s) for s in d]))
            count += num

    print(count)


part_one()
part_two()
