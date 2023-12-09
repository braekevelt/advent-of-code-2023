
with open('src/9/input.txt') as file:
    total = 0
    for line in file:
        sequence = list(map(int, line.strip().split()))
        number = 0
        while any(sequence):
            number += sequence[-1]
            sequence = [b - a for a, b in zip(sequence, sequence[1:])]
        total += number
    print(total)
