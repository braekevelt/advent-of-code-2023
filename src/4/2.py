
with open('src/4/input.txt') as file:
    cardCounts = dict()
    for line in file:
        card, numbers = line.split(':', 1)
        _, cardId = card.split(' ', 1)
        cardId = int(cardId)
        winning, yours = map(str.split, numbers.split('|', 1))
        correct = len([number for number in winning if number in yours])
        amount = 1 + cardCounts.get(cardId, 0)
        cardCounts[cardId] = amount
        for nextCardId in range(cardId + 1, cardId + 1 + correct):
            cardCounts[nextCardId] = amount + cardCounts.get(nextCardId, 0)
    print(sum(cardCounts.values()))
