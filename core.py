# core.py

GRID_SIZE = 9
BLOCK_SIZE = 3

def empty_grid():
    return [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def is_valid(grid):
    return check_row(grid) and check_col(grid) and check_block(grid)

def check_row(grid):
    for row in grid:
        if set(row) != set(range(1, 10)):
            return False
    return True

def check_col(grid):
    for c in range(9):
        col = [grid[r][c] for r in range(9)]
        if set(col) != set(range(1, 10)):
            return False
    return True

def check_block(grid):
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            block = [
                grid[r][c]
                for r in range(br, br + 3)
                for c in range(bc, bc + 3)
            ]
            if set(block) != set(range(1, 10)):
                return False
    return True
