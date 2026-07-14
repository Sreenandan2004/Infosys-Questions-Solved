# Distinct Frequency Pairs Explainer

## Problem Description & Example Test Case
Given an array $A$ of length $N$. Find the number of pairs $(i, j)$ with $1 \le i < j \le N$ such that:
$$\text{frequency}(1, i, A[i]) + \text{frequency}(j, N, A[j]) \le \lfloor \text{distinct}(1, i) / 2 \rfloor + \lfloor \text{distinct}(j, N) / 2 \rfloor$$

### Example Test Case
Input: $N=3, A=[1, 1, 2]$.
Output: 1 (pair $(1, 3)$).

---

## Prerequisite Concepts
- **Fenwick Tree (Binary Indexed Tree):** To count elements $\le x$ in $O(\log N)$ time.
- **Coordinate Compression:** Mapping arbitrary real values to indices $1 \dots U$.

---

## The Naive Approach
Iterate over all pairs $i < j$, compute the frequencies and distinct counts in $O(N)$ for each pair, and check the condition.
- **Time Complexity:** $O(N^3)$
- **Space Complexity:** $O(N)$

---

## The Optimal Approach
Let:
- $F_{left}[i] = \text{frequency}(1, i, A[i])$
- $D_{left}[i] = \lfloor \text{distinct}(1, i) / 2 \rfloor$
- $F_{right}[j] = \text{frequency}(j, N, A[j])$
- $D_{right}[j] = \lfloor \text{distinct}(j, N) / 2 \rfloor$

We can precompute these values in $O(N)$ time.
The condition is:
$$F_{left}[i] + F_{right}[j] \le D_{left}[i] + D_{right}[j] \implies F_{left}[i] - D_{left}[i] \le D_{right}[j] - F_{right}[j]$$
Let $val_{left}[i] = F_{left}[i] - D_{left}[i]$ and $val_{right}[j] = D_{right}[j] - F_{right}[j]$.
We want to count pairs $i < j$ where $val_{left}[i] \le val_{right}[j]$.
We use coordinate compression on the values and count them using a Fenwick Tree as we iterate $j$ from 0 to $N-1$.

---

## Optimal Complexity Breakdown
- **Time Complexity:** $O(N \log N)$
- **Space Complexity:** $O(N)$

---

## Pseudocode
```text
val_left = [F_left[i] - D_left[i] for i in range(N)]
val_right = [D_right[j] - F_right[j] for j in range(N)]
compress(val_left, val_right)
bit = Fenwick Tree
ans = 0
for j from 0 to N-1:
    ans += query(bit, val_right[j])
    add(bit, val_left[j], 1)
```
