file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

seeds = []
maps = {}
key = ""
for line in myin:
    if line.__contains__("seeds"):
        seeds = [int(x) for x in line[line.index(":") + 2:].split(" ")]
    elif line.__contains__("map"):
        key = line[:line.index("map") - 1]
        maps[key] = []
    elif line:
        maps[key] = maps[key] + [[int(x) for x in line.split(" ")]]


def part_one():
    locations = []
    for seed in seeds:
        for m in maps:
            for l in maps[m]:
                if l[1] <= seed < l[1] + l[2]:
                    seed = seed - l[1] + l[0]
                    break
        locations.append(seed)
    print(min(locations))


def part_two():
    # start from a location number, and find a valid seed
    location = 0

    while True:
        seed = location
        # translate a location into seed by swapping source and destination
        for m in list(maps.keys())[::-1]:
            for l in maps[m]:
                if l[0] <= seed < l[0] + l[2]:
                    seed = seed - l[0] + l[1]
                    break

        found = False
        for i in range(0, len(seeds), 2):
            if seeds[i] <= seed < seeds[i] + seeds[i + 1]:
                found = True
                break

        if found:
            print(location)
            break
        location += 1


part_one()
part_two()
