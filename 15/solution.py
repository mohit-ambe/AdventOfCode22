file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def rfind(l, t):
    i = -1
    while i >= -len(l):
        if l[i] == t:
            return len(l) + i
        i -= 1
    return -1


def speak(times):
    nums = [int(x) for x in myin[0].split(",")]
    last = {nums[i]: i + 1 for i in range(len(nums))}
    prelast = {nums[i]: 0 for i in range(len(nums))}
    freq = {nums[i]: 1 for i in range(len(nums))}
    turn = len(nums)
    recent = nums[-1]
    while turn < times:
        turn += 1
        if freq.get(recent, 0) == 1:
            recent = 0
        else:
            recent = last[recent] - prelast[recent]
        freq[recent] = freq.get(recent, 0) + 1
        prelast[recent] = last.get(recent, turn)
        last[recent] = turn
    return recent


def part_one():
    print(speak(2020))


def part_two():
    print(speak(30000000))


part_one()
part_two()
