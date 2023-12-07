
charOrder = 'J23456789TQKA'

def charKey(char: str):
    return charOrder.index(char)

def handKey(hand: str):
    keys = [charKey(char) for char in hand]
    jokerValue = max([char for char in hand if char != 'J'] + ['A'], key=lambda x: hand.count(x))
    jokerHand = hand.replace('J', jokerValue)
    counts = sorted((jokerHand.count(char) for char in jokerHand), reverse=True)
    return counts + keys

def pairKey(pair: list[str, str]):
    return handKey(pair[0])

with open('src/7/input.txt') as file:
    pairs = sorted((line.strip().split(None, 1) for line in file if line), key=pairKey)
    print(sum(rank * int(bid) for rank, (_, bid) in enumerate(pairs, 1)))
