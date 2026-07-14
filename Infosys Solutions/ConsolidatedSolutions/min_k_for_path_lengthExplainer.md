# Min K for Path Length Explainer

## Problem Description & Example Test Case
Given a permutation $p$ of length $n$ and an integer $m$. A directed edge $i \to j$ exists if $p[i] < p[j]$ and $|i - j| \le k$.
Find the minimum $k$ such that the directed graph contains a path of length $\ge m$ (i.e. containing $\ge m$ nodes).

### Example Test Case
Input: $n=3, m=2, p=[1, 3, 2]$.
Output: 1 (for $k=1$, edge $1 \to 3$ exists ($p[1]=1 < p[3]=2$, $|1-3|=2 \not\le 1$), and $1 \to 2$ exists, path $1 \to 2$ has 2 nodes).

---

## Prerequisite Concepts
- **Binary Search on Answer:** Searching for the minimum $k$ in range $[0, n-1]$.
- **Longest Path in DAG:** Standard dynamic programming on DAG.
- **Segment Tree:** Querying range maximums of DP values.

---

## The Naive Approach
For each $k$, build the adjacency list and find the longest path using DFS/BFS.
- **Time Complexity:** $O(N \cdot (N + E))$ where $E \approx N \cdot k$.
- **Space Complexity:** $O(N \cdot k)$

---

## The Optimal Approach
Since the condition "longest path $\ge m$" is monotonic with $k$, we binary search for $k$.
For a fixed $k$, we compute the longest path ending at each node using DP:
$$dp[i] = 1 + \max_{p[j] < p[i], |i - j| \le k} dp[j]$$
To do this in $O(N \log N)$ time:
- Sort the indices by their values $p[i]$ and process nodes in increasing order.
- When processing node $i$, all candidate nodes $j$ with $p[j] < p[i]$ have already been processed and their $dp[j]$ values are set.
- We query the maximum of $dp[j]$ in the index range $[i-k, i+k]$ using a Segment Tree, and update the Segment Tree at position $i$ with $dp[i]$.

---

## Optimal Complexity Breakdown
- **Time Complexity:** $O(N \log^2 N)$
- **Space Complexity:** $O(N)$

---

## Pseudocode
```text
function check(k):
    nodes = sorted list of (p[i], i)
    tree = Segment Tree over indices 0..n-1
    for val, idx in nodes:
        l = max(0, idx - k), r = min(n - 1, idx + k)
        dp[idx] = query_max(tree, l, r) + 1
        if dp[idx] >= m: return True
        update_tree(tree, idx, dp[idx])
    return False
```
