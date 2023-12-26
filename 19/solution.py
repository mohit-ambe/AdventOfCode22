import re

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

workflows = {}
ratings = []

for line in myin:
    if line.startswith("{"):
        line = line.replace("{", "{\"").replace(",", ",\"")
        line = line.replace("=", "\"=").replace("=", ":")
        ratings.append(eval(line))
    else:
        workflows[line[:line.find("{")]] = line[line.find("{") + 1:-1].split(",")


def process_part(flow, rating):
    if flow == "A":
        return True
    if flow == "R":
        return False
    for i, rule in enumerate(workflows[flow]):
        if ":" in rule:
            check, dest = rule.split(":")
            key = re.findall('[xmas]', check)[0]
            if eval(check.replace(key, str(rating[key]))):
                return process_part(dest, rating)
        else:
            return process_part(rule, rating)


def part_one():
    ans = 0
    flow = "in"
    for r in ratings:
        if process_part(flow, r):
            ans += sum(r.values())
    print(ans)


def part_two():
    ans = 0
    Q = [("in", 1, 4000, 1, 4000, 1, 4000, 1, 4000)]
    seen = set()
    while Q:
        key, xl, xh, ml, mh, al, ah, sl, sh = Q.pop(0)
        if key == 'A':
            ans += (xh - xl + 1) * (mh - ml + 1) * (ah - al + 1) * (sh - sl + 1)
            continue
        if key == 'R' or key in seen:
            continue
        seen.add(key)
        for i, rule in enumerate(workflows[key]):
            if ":" in rule:
                check, dest = rule.split(":")
                num = int(re.findall("\d+", check)[0])
                rating = re.findall('[xmas]', check)
                state = [dest, xl, xh, ml, mh, al, ah, sl, sh]
                if "<" in check:
                    if 'x' in rating:
                        state[2] = num - 1
                        xl = num
                    if 'm' in rating:
                        state[4] = num - 1
                        ml = num
                    if 'a' in rating:
                        state[6] = num - 1
                        al = num
                    if 's' in rating:
                        state[8] = num - 1
                        sl = num
                if ">" in check:
                    if 'x' in rating:
                        state[1] = num + 1
                        xh = num
                    if 'm' in rating:
                        state[3] = num + 1
                        mh = num
                    if 'a' in rating:
                        state[5] = num + 1
                        ah = num
                    if 's' in rating:
                        state[7] = num + 1
                        sh = num
                Q.append(tuple(state))
            else:
                Q.append(tuple([rule, xl, xh, ml, mh, al, ah, sl, sh]))
    print(ans)


part_one()
part_two()
