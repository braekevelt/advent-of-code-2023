
with open('src/4/input.txt') as file:
    total = 0
    for line in file:
        _, numbers = line.split(':', 1)
        winning, yours = map(str.split, numbers.split('|', 1))
        correct = len([number for number in winning if number in yours])
        total += 2 ** (correct - 1) if correct > 0 else 0
    print(total)
