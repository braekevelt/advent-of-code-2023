
with open('src/15/input.txt') as file:
    total = 0
    for step in file.read().strip().split(','):
        current = 0
        for char in step:
            current += ord(char)
            current *= 17
            current %= 256
        total += current
    print(total)
