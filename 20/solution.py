file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

tree = dict()
module = dict()
on = set()
pulses = dict()
conjunct = dict()

for line in myin:
    k, v = line.split(" -> ")
    key = "".join([ch for ch in k if ch not in "%&"])
    tree[key] = v.split(", ")

    if "%" in k:
        module[key] = 'ff'
    elif "&" in k:
        module[key] = 'cj'
        conjunct[key] = []
        for l in myin:
            if l == line:
                continue
            if key in l:
                inp, _ = l.split(" -> ")
                inp = "".join([c for c in inp if c not in "%&"])
                conjunct[key].append(inp)
    else:
        module[key] = "bc"

low = 0
high = 0


def push(target=(None, None)):
    global low, high
    # low pulse is false
    Q = [("broadcaster", False)]
    while Q:
        if target in Q:
            return True
        key, pulse = Q.pop(0)
        if pulse:
            high += 1
        else:
            low += 1
        if key not in tree:
            continue
        if module[key] == "bc":
            Q.extend([(child, pulse) for child in tree[key]])
        elif module[key] == "ff":
            if not pulse:
                if key in on:
                    on.discard(key)
                elif key not in on:
                    on.add(key)
                pulse = (key in on)
                Q.extend([(child, pulse) for child in tree[key]])
            else:
                continue
        elif module[key] == 'cj':
            if len(conjunct[key]) == 1:
                child = tree[key][0]
                pulse = not pulse
                Q.append((child, pulse))
            else:
                pulse = False if all((f in pulses and pulses[f]) for f in conjunct[key]) else True
                Q.extend([(child, pulse) for child in tree[key]])

        for child in tree[key]:
            if child in module and module[child] == 'cj':
                pulses[key] = pulse
    return False


def part_one():
    global low, high
    for i in range(1000):
        push()
    print(low * high)


def part_two():
    global on, pulses
    ans = 1
    # manually found 4 conjuncts to send low to conjunct to send low to rx
    # lcm of button presses for these 4 gives the answer
    for t in [("dh", False), ("qd", False), ("bb", False), ("dp", False)]:
        pulses.clear()
        on.clear()
        i = 0
        b = False
        while not b:
            i += 1
            b = push(t)
        ans *= i
    print(ans)


part_one()
part_two()
