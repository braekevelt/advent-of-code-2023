
def countEnergized(grid: tuple[str], beam: tuple[int, int, int, int]):
    energized = set()
    directions = set()
    stack = [beam]
    while stack:
        row, col, drow, dcol = stack.pop()
        
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            continue
        elif ((row, col, drow, dcol)) in directions:
            continue
        else:
            energized.add((row, col))
            directions.add((row, col, drow, dcol))

        match (grid[row][col]):
            case '.':
                stack.append((row + drow, col + dcol, drow, dcol))
            case '/':
                stack.append((row - dcol, col - drow, -dcol, -drow))
            case '\\':
                stack.append((row + dcol, col + drow, dcol, drow))
            case '-':
                if drow == 0:
                    stack.append((row + drow, col + dcol, drow, dcol))
                else:
                    stack.append((row - dcol, col - drow, -dcol, -drow))
                    stack.append((row + dcol, col + drow, dcol, drow))
            case '|':
                if dcol == 0:
                    stack.append((row + drow, col + dcol, drow, dcol))
                else:
                    stack.append((row - dcol, col - drow, -dcol, -drow))
                    stack.append((row + dcol, col + drow, dcol, drow))

    return len(energized)

with open('src/16/input.txt') as file:
    grid = tuple(line.strip() for line in file if not line.isspace())
    rows = len(grid)
    cols = len(grid[0])
    left = max(countEnergized(grid, (row, 0, 0, 1)) for row in range(rows))
    right = max(countEnergized(grid, (row, cols - 1, 0, -1)) for row in range(rows))
    top = max(countEnergized(grid, (0, col, 1, 0)) for col in range(cols))
    bottom = max(countEnergized(grid, (rows - 1, col, -1, 0)) for col in range(cols))
    print(max(left, right, top, bottom))
