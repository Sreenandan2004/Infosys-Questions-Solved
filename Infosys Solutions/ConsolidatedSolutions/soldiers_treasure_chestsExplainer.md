# Soldiers & Treasure Chests Explainer

## Problem Description & Example Test Case
There are $N$ soldiers. Node $i$ has power $A[i] \le N/2$ and $Bonus[i]$ XP.
For each soldier $i$:
- Find the first soldier $R > i$ such that $A[R]$ is a multiple of $A[i]$.
- If such $R$ exists, Bob gets $\max_{j \in [i, R]} Bonus[j]$ XP.
Find the total XP Bob gets.

### Example Test Case
Input: $N=3, A=[1, 2, 2], Bonus=[10, 5, 20]$.
Output: 30 (for $i=0$: first multiple of 1 is at $R=1$ (value 2), max bonus in $[0, 1]$ is 10. For $i=1$: first multiple of 2 is at $R=2$ (value 2), max bonus in $[1, 2]$ is 20).

---

## Prerequisite Concepts
- **Sparse Table:** To answer Range Maximum Queries (RMQ) in $O(1)$ time after $O(N \log N)$ preprocessing.
- **Divisor/Multiple Search:** Finding the closest occurrence of multiples using an index directory.

---

## The Naive Approach
For each $i$, scan to the right to find the first multiple, then iterate over $[i, R]$ to find the max bonus.
- **Time Complexity:** $O(N^2)$
- **Space Complexity:** $O(1)$

---

## The Optimal Approach
We build a Sparse Table on the `Bonus` array. This allows us to answer $\max_{j \in [i, R]} Bonus[j]$ in $O(1)$ time.
To find the first index $R > i$ containing a multiple of $A[i]$:
- We process the array from right to left.
- We maintain `pos[x]`, which stores the first index to the right containing value $x$.
- When we are at $i$:
  We look up `pos[m]` for all multiples $m = c \cdot A[i]$ up to $N/2$, and take $R = \min pos[m]$.
  The sum of the number of multiples over all values $1 \dots N/2$ is bounded by $O(N \log N)$.
- We query the Sparse Table for the range $[i, R]$ and update `pos[A[i]] = i`.

---

## Optimal Complexity Breakdown
- **Time Complexity:** $O(N \log N)$
- **Space Complexity:** $O(N \log N)$

---

## Pseudocode
```text
st = Sparse Table on Bonus
pos = array of size N//2 + 1 initialized to infinity
total_xp = 0
for i from N-1 down to 0:
    v = A[i]
    r_index = min(pos[m] for m in range(v, N//2 + 1, v))
    if r_index != infinity:
        total_xp += query_max(st, i, r_index)
    pos[v] = i
```
