
start = None
graph = dict()

with open('src/10/input.txt') as file:
    grid = [line.strip() for line in file if not line.isspace()]
    rows = len(grid)
    cols = len(grid[0])
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
            
print(len(longestPath) // 2)
