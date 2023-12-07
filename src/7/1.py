
charOrder = '23456789TJQKA'

def charKey(char: str):
    return charOrder.index(char)

def handKey(hand: str):
    keys = [charKey(char) for char in hand]
    counts = sorted((hand.count(char) for char in hand), reverse=True)
    return counts + keys

def pairKey(pair: list[str, str]):
    return handKey(pair[0])

with open('src/7/input.txt') as file:
    pairs = sorted((line.strip().split(None, 1) for line in file), key=pairKey)
    print(sum(rank * int(bid) for rank, (_, bid) in enumerate(pairs, 1)))
