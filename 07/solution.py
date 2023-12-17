file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

cards = [line[:line.index(" ")] for line in myin]
# for easier sorting
for k, s in enumerate(cards):
    s = s.replace("A", "E")
    s = s.replace("K", "D")
    s = s.replace("Q", "C")
    s = s.replace("J", "B")
    s = s.replace("T", "A")
    cards[k] = s

nums = [int(line[line.index(" ") + 1:]) for line in myin]

card_dict = dict(zip(cards, nums))


def get_rank(card, p2=False):
    if p2:
        if card == "BBBBB":
            return 7
        max_card = ""
        max_count = 0
        for c in card:
            if card.count(c) > max_count and c != "B":
                max_count = card.count(c)
                max_card = c
        card = card.replace("B", max_card)

    repeats = tuple(sorted([card.count(c) for c in set([x for x in card])]))
    if repeats == (5,):
        return 7
    if repeats == (1, 4):
        return 6
    if repeats == (2, 3):
        return 5
    if repeats == (1, 1, 3):
        return 4
    if repeats == (1, 2, 2):
        return 3
    if repeats == (1, 1, 1, 2):
        return 2
    if repeats == (1, 1, 1, 1, 1):
        return 1


def part_one():
    cards_with_rank = [(card, get_rank(card)) for card in list(card_dict.keys())]
    cards_with_rank = sorted(cards_with_rank, key=lambda x:x[1])

    cards_ranked = []
    for rank in range(1, 7 + 1):
        cards_ranked.extend(sorted([c for c, r in cards_with_rank if r == rank]))

    print(sum([card_dict[card] * (i + 1) for i, card in enumerate(cards_ranked)]))


def part_two():
    cards_with_rank = [(card, get_rank(card, True)) for card in list(card_dict.keys())]
    cards_with_rank = sorted(cards_with_rank, key=lambda x:x[1])

    cards_ranked = []
    for rank in range(1, 7 + 2):
        cards_ranked.extend(sorted([c.replace("B", "0") for c, r in cards_with_rank if r == rank]))

    print(sum([card_dict[card.replace("0", "B")] * (i + 1) for i, card in enumerate(cards_ranked)]))


part_one()
part_two()
