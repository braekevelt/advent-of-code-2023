
with open('src/11/input.txt') as file:
    lines = file.readlines()

    galaxies = [
        (row, col)
        for row, line in enumerate(lines)
        for col, char in enumerate(line)
        if char == '#'
    ]

    rows, cols = zip(*galaxies)

    for index in range(len(lines) - 1, -1, -1):
        if index not in rows:
            galaxies = [(row + 999999 if row > index else row, col) for row, col in galaxies]
    
    for index in range(len(lines[0]) - 1, -1, -1):
        if index not in cols:
            galaxies = [(row, col + 999999 if col > index else col) for row, col in galaxies]
    
    lengths = [abs(a - c) + abs(b - d) for a, b in galaxies for c, d in galaxies if a != c or b != d]
    print(sum(lengths) // 2)
