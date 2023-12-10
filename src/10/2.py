
grid = []
with open('src/10/input.txt') as file:
    grid = [line.strip() for line in file if not line.isspace()]

rows = len(grid)
cols = len(grid[0])

start = None
graph = dict()

for row, line in enumerate(grid):
    for col, char in enumerate(line):
        top = (row - 1, col)
        bottom = (row + 1, col)
        left = (row, col - 1)
        right = (row, col + 1)
        match char:
            case '|':
                graph[(row, col)] = (top, bottom)
            case '-':
                graph[(row, col)] = (left, right)
            case 'L':
                graph[(row, col)] = (top, right)
            case 'J':
                graph[(row, col)] = (top, left)
            case '7':
                graph[(row, col)] = (left, bottom)
            case 'F':
                graph[(row, col)] = (right, bottom)
            case 'S':
                start = (row, col)
                graph[(row, col)] = (left, right, top, bottom)

longestPath = (start,)
stack = [longestPath]

while stack:
    previousPath = stack.pop()
    previousNode = previousPath[-1]
    for node in graph.get(previousNode, ()):
        if node == start:
            if len(longestPath) < len(previousPath):
                longestPath = previousPath
        elif node in graph and node not in previousPath:
            path = (*previousPath, node)
            stack.append(path)

startChar = None
last = longestPath[-1]
second = longestPath[1]
isAbove = second[0] < last[0]
isBelow = second[0] > last[0]
isLeft = second[1] < last[1]
isRight = second[1] > last[1]
if isAbove:
    if isLeft:
        startChar = 'L'
    elif isRight:
        startChar = 'J'
    else:
        startChar = '|'
elif isBelow:
    if isLeft:
        startChar = 'F'
    elif isRight:
        startChar = '7'
    else:
        startChar = '|'
else:
    startChar = '-'

countInsideLoop = 0
with open('src/10/output.txt', 'w') as file:
    for row in range(rows):
        isInside = False
        openingChar = None
        for col in range(cols):
            if (row, col) in longestPath:
                char = grid[row][col]
                if char == 'S':
                    char = startChar
                file.write(char)
                if char == '|':
                    isInside = not isInside
                elif char == 'L':
                    openingChar = char
                elif openingChar == 'L' and char == '7':
                    isInside = not isInside
                    openingChar = None
                elif char == 'F':
                    openingChar = char
                elif openingChar == 'F' and char == 'J':
                    isInside = not isInside
                    openingChar = None
            elif isInside:
                countInsideLoop += 1
                file.write('.')
            else:
                file.write(' ')
        file.write('\n')

print(countInsideLoop)
