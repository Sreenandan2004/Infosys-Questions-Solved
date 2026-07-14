# BFS on Circular Jumps Explainer

## Problem Description & Example Test Case
$N$ people sit around a circular table. From chair $i$, a person can jump $A[i]$ chairs left or right in one jump.
Find the minimum jumps Bob needs to get from chair $X$ to chair $Y$. If impossible, return -1.

### Example Test Case
Input: $N=5, X=5, Y=1, A=[1, 2, 3, 2, 4]$.
Output: 1 (jump $A[5]=4$ positions left from 5 to reach 1).

---

## Prerequisite Concepts
- **Breadth-First Search (BFS):** To find the shortest path in an unweighted graph.
- **Circular Modulo Arithmetic:** Index transitions on a circle of size $N$ (1-indexed).

---

## The Naive Approach
A depth-first search (DFS) that explores all path combinations, which can get stuck in cycles.
- **Time Complexity:** $O(2^N)$
- **Space Complexity:** $O(N)$

---

## The Optimal Approach
We build the transition graph dynamically and run a BFS.
From chair $u$:
- Jump right: $(u + A[u] - 1) \pmod N + 1$
- Jump left: $(u - A[u] - 1) \pmod N + 1$
We run a standard queue-based BFS starting at $X$. The first time we dequeue $Y$, we return the distance. If the queue becomes empty and we haven't reached $Y$, we return -1.

---

## Optimal Complexity Breakdown
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$

---

## Pseudocode
```text
dist = array of size N+1 initialized to -1
dist[X] = 0
q = queue containing [X]

while q is not empty:
    curr = q.pop()
    right = (curr + A[curr] - 1) % N + 1
    left = (curr - A[curr] - 1) % N + 1
    for neighbor in (right, left):
        if dist[neighbor] == -1:
            dist[neighbor] = dist[curr] + 1
            if neighbor == Y: return dist[neighbor]
            q.push(neighbor)
return -1
```
