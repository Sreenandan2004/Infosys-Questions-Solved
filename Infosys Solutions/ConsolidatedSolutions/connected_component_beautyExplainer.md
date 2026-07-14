# Graph Component Beauty Explainer

## Problem Description & Example Test Case
You have a graph of $n$ nodes, initially disconnected. Node $i$ has value $i$.
`beauty(S)` is the minimum number of covered ranges in $S$. For example: `beauty([1, 2, 4, 5, 8, 11]) = 4` (ranges are $[1, 2], [4, 5], [8], [11]$).
Queries:
1. `(1, u, v)`: Add edge between $u$ and $v$.
2. `(2, u, 0)`: Find the beauty of the connected component of $u$.

Find the sum of answers to all Type 2 queries.

### Example Test Case
Input: $n=2, q=1, \text{queries} = [[2, 1, 0]]$.
Output: 1.

---

## Prerequisite Concepts
- **Disjoint Set Union (DSU) / Union-Find:** To maintain connected components.
- **Small-to-Large Merging:** A technique to merge sets of size $S_1 < S_2$ in $O(S_1)$ time, yielding $O(N \log N)$ total time.

---

## The Naive Approach
Whenever a query is processed, run a DFS to find the set of nodes in $u$'s component, sort them, and count the number of contiguous segments.
- **Time Complexity:** $O(Q \cdot N \log N)$
- **Space Complexity:** $O(N)$

---

## The Optimal Approach
We can represent the beauty of a set $S$ as:
$$\text{beauty}(S) = |S| - (\text{number of consecutive pairs } (x, x+1) \in S)$$
We use DSU to maintain components. For each component root, we store its size, the set of elements it contains, and the number of consecutive pairs.
When merging two components $C_1$ and $C_2$:
- We merge their sizes.
- We iterate over the elements of the smaller component (small-to-large merging). For each $x$, we check if $x-1$ or $x+1$ is in the larger component. If so, we increment the consecutive pairs count.
- The total time spent iterating is $O(N \log N)$ across the entire algorithm.

---

## Optimal Complexity Breakdown
- **Time Complexity:** $O(N \log^2 N)$ (using Python sets)
- **Space Complexity:** $O(N)$

---

## Pseudocode
```text
class DSU:
    def union(u, v):
        ru = find(u), rv = find(v)
        if ru != rv:
            if size[ru] < size[rv]: swap(ru, rv)
            parent[rv] = ru
            size[ru] += size[rv]
            new_pairs = 0
            for x in elements[rv]:
                if x-1 in elements[ru]: new_pairs += 1
                if x+1 in elements[ru]: new_pairs += 1
            consecutive_pairs[ru] += consecutive_pairs[rv] + new_pairs
            elements[ru].update(elements[rv])
```
