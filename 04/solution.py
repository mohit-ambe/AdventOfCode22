from functools import cache

file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

cards = [line[line.index(":") + 2:] for line in myin]
winning_numbers = []


def part_one():
    points = 0

    for card in cards:
        card = card.replace("  ", " ").strip()
        win, mine = [[int(x) for x in half.split(" ")] for half in card.split(" | ")]
        my_winning = [num for num in win if num in mine]

        winning_numbers.append(len(my_winning))
        if my_winning:
            points += 2 ** (len(my_winning) - 1)

    print(points)


@cache
def play_cards(i):
    cards_won = winning_numbers[i]

    for card in range(i + 1, i + 1 + winning_numbers[i]):
        cards_won += play_cards(card)

    return cards_won


def part_two():
    print(len(cards) + sum([play_cards(i) for i in range(len(cards))]))


part_one()
part_two()
