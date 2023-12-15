
def load(lines: tuple[tuple[str]]) -> int:
    return sum (len(lines) - row for row, line in enumerate(lines) for char in line if char == 'O')

def shift(line: tuple[str]) -> tuple[str]:
    shifted = list(line)
    l = len(line)
    for _ in range(l):
        for i in range(l - 1):
            if shifted[i] == '.' and shifted[i + 1] == 'O':
                shifted[i] = 'O'
                shifted[i + 1] = '.'
    return tuple(shifted)

def transpose(lines: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return tuple(zip(*lines))

def west(lines: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return tuple(shift(line) for line in lines)

def north(lines: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return transpose(west(transpose(lines)))

def south(lines: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return north(lines[::-1])[::-1]

def east(lines: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return transpose(south(transpose(lines)))

def cycle(lines: tuple[tuple[str]]) -> tuple[tuple[str]]:
    return east(south(west(north(lines))))

with open('src/14/input.txt') as file:
    lines = tuple(tuple(line.strip()) for line in file if not line.isspace())
    cycles = []
    while lines not in cycles:
        cycles.append(lines)
        lines = cycle(lines)
    first = cycles.index(lines)
    index = first + ((1000000000 - first) % (len(cycles) - first))
    print(load(cycles[index]))
