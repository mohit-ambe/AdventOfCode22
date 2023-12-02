import time
from sympy import *

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

jobs = {}

for line in myin:
    jobs[line[:line.index(":")]] = line[line.index(":") + 2:]


def part_one():
    yell = "root"
    while (any([y.isalpha() for y in yell])):
        for j in jobs:
            if j in yell:
                yell = yell.replace(j, "({})".format(jobs[j]))
    print(int(eval(yell)))


def part_two():
    equation = ""
    for term in jobs["root"].split(" "):
        if not term.isalpha():
            continue
        yell = term
        while (any([y.isalpha() for y in yell.replace("humn","")])):
            for j in jobs:
                if j in yell and j != "humn":
                    yell = yell.replace(j, "({})".format(jobs[j]))
        equation += yell + "-" #arrange the equation: a=b -> a-b=0
    print(solve(parse_expr(equation[:-1]))[0]) #solve the express a-b=0, which is a=b


part_one()
part_two()
