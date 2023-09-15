from itertools import combinations
from functools import cache
from time import time

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

valves = dict()
rates = dict()

for line in myin:
    key = line.split(" ")[1]

    rate = line.split(" ")[4]
    rate = int(rate[rate.index("=") + 1:-1])

    vals = line.replace(",", "").split(" ")
    vals = vals[vals.index("to") + 2:]

    valves[key] = vals
    rates[key] = rate

valves_with_flow = [r for r in rates.keys() if rates[r] != 0]


@cache
def navigate(start, end, visited=()):
    visited = visited + (start,)
    if end in valves[start] or start == end:
        return 1
    else:
        n = [navigate(s, end, visited) for s in valves[start] if s not in visited]
        n.append(1e6 - 1)
        return 1 + min(n)


max_pressure = [0, 0]


def solve(start, unvisited, time_left, pressure, player=1):
    global max_pressure

    if time_left <= 0 or not unvisited:
        max_pressure[player - 1] = max(max_pressure[player - 1], pressure)
        return

    for valve in unvisited:
        next_time_left = max(time_left - navigate(start, valve) - 1, 0)
        next_pressure = pressure + next_time_left * rates[valve]
        solve(valve, [v for v in unvisited if v != valve], next_time_left, next_pressure, player)


def part_one():
    solve("AA", valves_with_flow, 30, 0)
    print(max_pressure[0])


def part_two():
    global max_pressure
    max_combined_pressure = 0

    for p in combinations(valves_with_flow, r=(len(valves_with_flow) // 2)):
        max_pressure = [0, 0]
        p1 = list(p)
        p2 = list(set(valves_with_flow) - set(p1))
        solve("AA", p1, 26, 0)
        solve("AA", p2, 26, 0, player=2)
        max_combined_pressure = max(max_combined_pressure, sum(max_pressure))

    print(max_combined_pressure)

part_one()
part_two()
