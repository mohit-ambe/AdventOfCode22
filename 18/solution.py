file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def evaluate(expr):
    if "(" not in expr:
        nums = 0
        modified = ""
        for char in expr.split(" "):
            if char.isdigit():
                nums += 1
                if nums != 1:
                    modified += char + ")"
                else:
                    modified += char
            else:
                modified += char
        return str(eval("(" * (nums - 1) + modified))
    else:
        terms = [""]
        opened = 0
        for char in expr:
            terms[-1] += char
            if char == "(":
                opened += 1
            elif char == ")":
                opened -= 1
                if not opened:
                    terms.append("")

        for i, term in enumerate(terms):
            if "(" in term:
                to_eval = term[term.find("("):term.rfind(")") + 1]
                terms[i] = term.replace(to_eval, evaluate(to_eval[1:-1]))

        return str(evaluate("".join(terms)))


def part_one():
    print(sum(int(evaluate(line)) for line in myin))


def part_two():
    print(sum(int(eval("({})".format(line.replace(" * ", ") * (")))) for line in myin))


part_one()
part_two()
