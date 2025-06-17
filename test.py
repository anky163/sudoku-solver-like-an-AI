from generator import generate
from utils import print_grid
from core import is_valid

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # row 0
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # row 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # row 2
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # row 3
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # row 4
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # row 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # row 6
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # row 7
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # row 8
]

generate(grid)
print_grid(grid)
print(is_valid(grid))