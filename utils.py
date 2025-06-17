# utils.py


def print_grid(grid):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 25)
        row = ""
        for c in range(9):
            if c % 3 == 0 and c != 0:
                row += " |"
            row += f" {grid[r][c]}"
        print(row)
