import random

base = 3
N = base * base

def candidates(grid, r, c):
    if grid[r][c] != 0:
        return []
    
    # Dò hàng của ô (r, c)
    cur_row = [x for x in grid[r][:] if x != 0]

    # Dò cột của ô (r, c)
    cur_col = [x for x in [grid[n][c] for n in range(N)] if x != 0]

    # Dò block của ô (r, c)
    br, bc = base * (r // base), base * (c // base)
    cur_block = [
        grid[i][j]
        for i in range(br, br + base)
        for j in range(bc, bc + base)
        if grid[i][j] != 0
    ]
    
    used = set(cur_row + cur_col + cur_block)
    return [x for x in range(1, N + 1) if x not in used]


def entropy_map(grid):
    entropy = {}
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                cand = candidates(grid, i, j)
                if cand:
                    entropy[(i, j)] = cand
    return entropy

def pick_lowest_entropy(entropy_map):
    if not entropy_map:
        return None

    min_len = min(len(c) for c in entropy_map.values())
    candidates = [pos for pos, opts in entropy_map.items() if len(opts) == min_len]
    return random.choice(candidates)