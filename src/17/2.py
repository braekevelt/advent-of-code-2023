from math import inf

with open('src/17/input.txt') as file:
    grid = tuple(
        tuple(int(char) for char in line.strip())
        for line in file
        if not line.isspace()
    )

    rows = len(grid)
    cols = len(grid[0])
    endRow = rows - 1
    endCol = cols - 1

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
            if direction != 'A' and count >= 4:
                neighbors.append((row - 1, col, 1, 'A'))
            elif direction == 'A' and count < 10:
                neighbors.append((row - 1, col, count + 1, 'A'))
        if row < endRow and direction != 'A':
            if direction != 'V' and count >= 4:
                neighbors.append((row + 1, col, 1, 'V'))
            elif direction == 'V' and count < 10:
                neighbors.append((row + 1, col, count + 1, 'V'))
        if col > 0 and direction != '>':
            if direction != '<' and count >= 4:
                neighbors.append((row, col - 1, 1, '<'))
            elif direction == '<' and count < 10:
                neighbors.append((row, col - 1, count + 1, '<'))
        if col < endCol and direction != '<':
            if direction != '>' and count >= 4:
                neighbors.append((row, col + 1, 1, '>'))
            elif direction == '>' and count < 10:
                neighbors.append((row, col + 1, count + 1, '>'))
        
        for neighbor in neighbors:
            r, c, _, _ = neighbor
            newLoss = loss + grid[r][c]
            if newLoss < losses.get(neighbor, inf):
                losses[neighbor] = newLoss
                if neighbor not in visited:
                    unvisited.add(neighbor)
    
    print(min(
        loss for (row, col, count, _), loss in losses.items()
        if row == endRow and col == endCol and count >= 4
    ))
