from math import prod

with open('src/2/input.txt') as file:
    total = 0
    for line in file:
        [game, subsets] = line.split(':', 1)
        [_, gameId] = game.split(' ', 1)
        bag = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for subset in subsets.split(';'):
            if not subset: continue
            for sample in subset.split(','):
                if not sample: continue
                [amount, color] = sample.strip().split(' ', 1)
                bag[color] = max(bag[color], int(amount))
        power = prod(bag.values())
        total += power
    print(total)
