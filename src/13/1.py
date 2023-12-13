
def getMirrors(lines):
    for linesBefore in range(1, len(lines)):
        if all(
            lines[linesBefore - 1 - index] == lines[linesBefore + index]
            for index in range(linesBefore)
            if linesBefore + index< len(lines)
        ):
            yield linesBefore

with open('src/13/input.txt') as file:
    total = 0
    for pattern in file.read().split('\n\n'):
        vertical = tuple(zip(*(line for line in pattern.split())))
        horizontal = tuple(tuple(line) for line in pattern.split())
        total += sum(getMirrors(vertical)) + 100 * sum(getMirrors(horizontal))
    print(total)
