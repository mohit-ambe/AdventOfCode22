import re
import time
from itertools import chain

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

blueprints = []
for line in myin:
    costs = re.findall("\d+", line)
    costs = [int(x) for x in costs]
    robot = dict(zip(["ore", "clay", "obsidian", "geode"],
                     [costs[1], costs[2], (costs[3], costs[4]), (costs[5], costs[6])]))
    blueprints.append(robot)

states = {}
geode_max = 0


def solve(robot_index, ore=0, clay=0, obsidian=0, geode=0, orebot=1, claybot=0, obsbot=0, geodebot=0, time=24):
    global geode_max
    key = (robot_index, ore, clay, obsidian, geode, orebot, claybot, obsbot, geodebot, time)
    if key in states.keys():
        geode_max = max(geode_max, states[key])
        return states[key]

    robo = blueprints[robot_index]

    if time == 0:
        geode_max = max(geode_max, geode)
        return geode

    # we can prune the search if geodes + geode bots * time + T(time) <= best total geodes.
    triangular = (time - 1) * (time) // 2
    if geode + time * geodebot + triangular <= geode_max:
        return geode

    if ore < 0 or clay < 0 or obsidian < 0 or geode < 0:
        geode_max = max(geode_max, geode)
        return geode

    if ore >= robo['geode'][0] and obsidian >= robo['geode'][1]:
        geo = solve(robot_index, ore - robo['geode'][0] + orebot, clay + claybot,
                    obsidian - robo['geode'][1] + obsbot, geode + geodebot, orebot,
                    claybot, obsbot, geodebot + 1, time - 1)

        states[key] = geo
        geode_max = max(geode_max, geo)
        return geo

    routes = []
    cost = list(robo.values())[:2] + list(chain.from_iterable(list(robo.values())[2:]))
    oremax, claymax, obsmax = (max(cost[:3]), cost[3], cost[5])

    if ore >= robo['obsidian'][0] and clay >= robo['obsidian'][1] and obsbot * time + obsidian < time * obsmax:
        routes.append(solve(robot_index, ore - robo['obsidian'][0] + orebot, clay - robo['obsidian'][1] + claybot,
                            obsidian + obsbot, geode + geodebot, orebot,
                            claybot, obsbot + 1, geodebot, time - 1))

    if ore >= robo['clay'] and claybot * time + clay < time * claymax:
        routes.append(solve(robot_index, ore - robo['clay'] + orebot, clay + claybot,
                            obsidian + obsbot, geode + geodebot, orebot,
                            claybot + 1, obsbot, geodebot, time - 1))

    if ore >= robo['ore'] and orebot * time + ore < time * oremax:
        routes.append(solve(robot_index, ore - robo['ore'] + orebot, clay + claybot,
                            obsidian + obsbot, geode + geodebot, orebot + 1,
                            claybot, obsbot, geodebot, time - 1))

    routes.append(solve(robot_index, ore + orebot, clay + claybot,
                        obsidian + obsbot, geode + geodebot, orebot,
                        claybot, obsbot, geodebot, time - 1))

    geo = max(routes)
    states[key] = geo
    geode_max = max(geode_max, geo)
    return geo


def part_one():
    global geode_max
    ans = 0
    for i in range(len(blueprints)):
        geode_max = 0
        ans += solve(i) * (i + 1)
    print(ans)


def part_two():
    global geode_max
    ans = 1
    for i in [0, 1, 2]:
        geode_max = 0
        ans *= solve(robot_index=i, time=32)
    print(ans)


part_one()
part_two()
