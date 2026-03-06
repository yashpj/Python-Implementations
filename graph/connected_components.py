def count_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(r, c):
        if (r, c) in visited:
            return
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != 1:
            return
        visited.add((r, c))
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count
