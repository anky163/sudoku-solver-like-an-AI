# generator.py

from entropy import entropy_map, pick_lowest_entropy
from core import is_valid
from random import shuffle

def generate(grid, on_step=None):
    if is_valid(grid):
        return True

    emap = entropy_map(grid)
    if not emap:
        return False

    cell = pick_lowest_entropy(emap)
    vals = emap[cell][:]
    shuffle(vals)
    r, c = cell

    for val in vals:
        grid[r][c] = val
        if on_step:
            on_step(r, c, val)
        if generate(grid, on_step):
            return True
        grid[r][c] = 0
        if on_step:
            on_step(r, c, 0)

    return False
