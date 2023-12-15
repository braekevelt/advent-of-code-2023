
with open('src/14/input.txt') as file:
    total = 0
    lines = [line for line in file if not line.isspace()]    
    colCounts = [len(lines)] * len(lines[0])
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == 'O':
                indexCount = colCounts[col]
                total += indexCount
                colCounts[col] = max(0, indexCount - 1)
            elif char == '#':
                colCounts[col] = max(0, len(lines) - 1 - row)
    print(total)
