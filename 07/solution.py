file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

pos = [int(x) for x in myin[0].split(",")]

def part_one():
    min_fuel = float("inf")
    for num in pos:
        min_fuel = min(min_fuel, sum([abs(p-num) for p in pos]))
    print(min_fuel)


def part_two():
    min_fuel = float("inf")
    for num in range(0,max(pos)):
        min_fuel = min(min_fuel, sum([(abs(p - num)) * (abs(p - num) + 1) // 2 for p in pos]))
    #   for the series n + (n+1) + (n+2) + ... --> sequence of partial sums = n * (n+1) / 2
    print(min_fuel)


part_one()
part_two()