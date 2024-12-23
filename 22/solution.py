file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()


def mix(secret, val):
    return secret ^ val


def prune(val):
    return val % 16777216


change_sequences = dict()
secret2000 = []
for num in list(map(int, myin)):
    changes = [num % 10]
    visited = set()
    for i in range(2000):
        num = prune(mix(num * 64, num))
        num = prune(mix(num // 32, num))
        num = prune(mix(num * 2048, num))
        change = num % 10 - sum(changes)
        changes.append(change)
        if i > 4:
            key = tuple(changes[i - 4:i])
            if key not in visited:
                change_sequences[key] = change_sequences.get(key, 0) + sum(changes[:-2])
                visited.add(key)
    secret2000.append(num)


def part_one():
    print(sum(secret2000))


def part_two():
    print(max(change_sequences.values()))


part_one()
part_two()
