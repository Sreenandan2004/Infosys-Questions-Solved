# Grid Invasion Explainer

## Problem Description & Example Test Case
An $N \times M$ grid contains:
- `*` (block)
- `A` (invaded cells)
- `E` (enemy cells)
At each second, any `E` adjacent to `A` is invaded (becomes `A`). Find the minimum time to invade all `E` cells. If impossible, return -1.

### Example Test Case
Input: $N=2, M=2$, grid = `["AE", "EE"]`.
Output: 2.

---

## Prerequisite Concepts
- **Grid Simulation:** Modifying state cell-by-cell in discrete time steps.

---

## The Chosen Approach (Naive)
We simulate the invasion second-by-second:
1. In each second, we scan the entire grid to find all enemy `E` cells that are adjacent to at least one invaded `A` cell.
2. If no such `E` cells are found, the invasion process has terminated.
3. Otherwise, we convert all these adjacent `E` cells to `A`, decrement our remaining enemy count, and increment our elapsed seconds.
4. If the process terminates and there are still uninvaded `E` cells, we return -1. Otherwise, we return the total seconds.

---

## Complexity Breakdown
- **Time Complexity:** $O((N \cdot M)^2)$ (in the worst case, we invade exactly 1 cell per second, requiring $N \cdot M$ scans of size $N \cdot M$)
- **Space Complexity:** $O(N \cdot M)$ (to store the grid)

---

## Pseudocode
```text
seconds = 0
while True:
    to_invade = []
    for each cell (r, c):
        if grid[r][c] == 'E' and is_adjacent_to_A(r, c):
            to_invade.append((r, c))
    if to_invade is empty:
        break
    for r, c in to_invade:
        grid[r][c] = 'A'
    seconds += 1
if remaining_E > 0: return -1
return seconds
```
