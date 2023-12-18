from math import inf

with open('src/17/input.txt') as file:
    grid = tuple(
        tuple(int(char) for char in line.strip())
        for line in file
        if not line.isspace()
    )

    endRow = len(grid) - 1
    endCol = len(grid[0]) - 1

    visited = set()
    unvisited = {(0, 0, 0, '>')}
    losses = {(0, 0, 0, '>'): 0}

    while unvisited:
        point = min(unvisited, key=lambda point: losses.get(point, inf))
        unvisited.remove(point)
        visited.add(point)

        loss = losses.get(point, inf)
        row, col, count, direction = point
        
        neighbors = []
        if row > 0 and direction != 'V':
            if direction != 'A':
                neighbors.append((row - 1, col, 1, 'A'))
            elif count < 3:
                neighbors.append((row - 1, col, count + 1, 'A'))
        if row < endRow and direction != 'A':
            if direction != 'V':
                neighbors.append((row + 1, col, 1, 'V'))
            elif count < 3:
                neighbors.append((row + 1, col, count + 1, 'V'))
        if col > 0 and direction != '>':
            if direction != '<':
                neighbors.append((row, col - 1, 1, '<'))
            elif count < 3:
                neighbors.append((row, col - 1, count + 1, '<'))
        if col < endCol and direction != '<':
            if direction != '>':
                neighbors.append((row, col + 1, 1, '>'))
            elif count < 3:
                neighbors.append((row, col + 1, count + 1, '>'))
        
        for neighbor in neighbors:
            r, c, _, _ = neighbor
            newLoss = loss + grid[r][c]
            if newLoss < losses.get(neighbor, inf):
                losses[neighbor] = newLoss
                if neighbor not in visited:
                    unvisited.add(neighbor)
    
    print(min(loss for (row, col, _, _), loss in losses.items() if row == endRow and col == endCol))
