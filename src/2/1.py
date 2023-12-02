
bag = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

with open('src/2/input.txt') as file:
    total = 0
    for line in file:
        [game, subsets] = line.split(':', 1)
        [_, gameId] = game.split(' ', 1)
        possible = True
        for subset in subsets.split(';'):
            if not subset: continue
            for sample in subset.split(','):
                if not sample: continue
                [amount, color] = sample.strip().split(' ', 1)
                if bag[color] < int(amount):
                    possible = False
        if possible:
            total += int(gameId)
    print(total)
