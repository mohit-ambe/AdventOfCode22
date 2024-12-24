file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

values = dict()
for line in myin[:myin.index("")]:
    k, v = line.split(": ")
    values[k] = int(v)

rules = []
for line in myin[myin.index("") + 1:]:
    line = line.replace("AND", "&")
    line = line.replace("XOR", "^")
    line = line.replace("OR", "|")
    line = line.replace(" -> ", " ")

    rules.append(line.split(" "))


def wiring(values, rules):
    z_values = sorted([k[-1] for k in rules if k[-1].startswith('z')])
    while any([True if z not in values else False for z in z_values]):
        for v1, op, v2, res in rules:
            if v1 in values and v2 in values:
                values[res] = eval(f'{values[v1]} {op} {values[v2]}')
    return "".join([str(values[z]) for z in z_values])[::-1]


def part_one():
    z_values = sorted([k[-1] for k in rules if k[-1].startswith('z')])
    while any([True if z not in values else False for z in z_values]):
        for v1, op, v2, res in rules:
            if v1 in values and v2 in values:
                values[res] = eval(f'{values[v1]} {op} {values[v2]}')
    binary = "".join([str(values[z]) for z in z_values])[::-1]
    print(int(binary, 2))


def part_two():
    print('dgr,dtv,fgc,mtj,vvm,z12,z29,z37')


# use dot language to visualize graph
# and find errors manually
# these are 'adder' logic structures

# op_code = {"|": "OR", "&": "AND", "^": "XOR"}
# print("strict digraph {")
# for v1, op, v2, res in rules:
#     print(f"  {v1} -> {res} [label={op_code[op]}]")
#     print(f"  {v2} -> {res} [label={op_code[op]}]")
# print("}")


part_one()
part_two()
