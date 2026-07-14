# Army Reduction Game Explainer

## Problem Description & Example Test Case
General Ali wants to reduce an enemy army of $N$ soldiers to just 1 soldier in minimal moves.
Moves:
1. $N \to N - 1$
2. $N \to \lceil N/2 \rceil$ (reduce by half floor)
3. $N \to \lceil N/3 \rceil$ (reduce by two-thirds floor)

Find the minimum number of moves.

### Example Test Case
Input: $N=5$.
Output: 3 (moves: $5 \to 3 \to 2 \to 1$).

---

## Prerequisite Concepts
- **Breadth-First Search (BFS):** To find the shortest path in a state transition graph.

---

## The Chosen Approach (Naive)
We use a standard **BFS (Breadth-First Search)** starting from the state $N$:
1. We push the starting state $N$ into a queue with move count 0.
2. At each step, we pop the current state and generate its three possible next states:
   - $curr - 1$
   - $(curr + 1) // 2$
   - $(curr + 2) // 3$
3. We push any unvisited next states into the queue and record them in a set of visited states to avoid cycles.
4. The first time we reach state 1, we return the number of moves.

---

## Complexity Breakdown
- **Time Complexity:** $O(N)$ (in the absolute worst case, but practically $O(\log^2 N)$ because division options shrink the search space exponentially)
- **Space Complexity:** $O(N)$

---

## Pseudocode
```text
q = queue containing (N, 0)
visited = set containing N
while q is not empty:
    curr, moves = q.pop()
    for next_val in [curr - 1, (curr + 1)//2, (curr + 2)//3]:
        if next_val == 1:
            return moves + 1
        if next_val not in visited:
            visited.add(next_val)
            q.push((next_val, moves + 1))
```
