# Max Subarray XOR Sum Explainer

## Problem Description & Example Test Case
Given an array $A$ of length $N$ and an integer $K$. Partition $A$ into contiguous subarrays, each of length $\ge K$.
The beauty of a subarray is the maximum XOR of a subset of elements in the subarray.
Find the maximum sum of beauties across the partition.

### Example Test Case
Input: $N=4, K=2, A=[1, 2, 4, 8]$.
Output: 15 (partition into $[1, 2]$ (beauty 3) and $[4, 8]$ (beauty 12)).

---

## Prerequisite Concepts
- **Linear Basis:** A structure that represents the span of a set of vectors under XOR in $O(\log (\max A))$ size.
- **Dynamic Programming (DP):** Storing partition state.
- **Segment Tree:** Querying range maximums.

---

## The Naive Approach
A DP where $dp[i] = \max_{j \le i-K} (dp[j] + \text{beauty}(A[j..i-1]))$, calculating the basis from scratch for each subarray.
- **Time Complexity:** $O(N^2 \cdot \log(\max A))$
- **Space Complexity:** $O(N)$

---

## The Optimal Approach
As we move from $i-1$ to $i$, the suffix linear basis can change values at most $\log(\max A) \approx 18$ times because the basis dimension is at most 18.
We maintain the suffix linear basis ending at $i$ along with the largest start index for each basis element. This allows us to partition the start indices $j$ into at most 18 intervals where the basis (and thus the beauty) is constant.
Within each interval $[L, R]$, we query the maximum of $dp[j]$ using a Segment Tree. This gives the transition $dp[i] = \max (dp[j] + \text{beauty})$ in $O(\log(\max A) \cdot \log N)$ time per step.

---

## Optimal Complexity Breakdown
- **Time Complexity:** $O(N \cdot \log(\max A) \cdot \log N)$
- **Space Complexity:** $O(N)$

---

## Pseudocode
```text
dp = array of size N+1
tree = Segment Tree on dp
basis = list of (val, idx) pairs of size 20
for i from 1 to N:
    insert (A[i-1], i-1) into basis, swapping smaller indices to maximize indices
    active = sorted active indices in basis in descending order
    for each interval between transition points:
        left = idx, right = min(last_idx, i - K)
        if left <= right:
            dp[i] = max(dp[i], query_max(tree, left, right) + max_xor(curr_basis))
    update_tree(tree, i, dp[i])
```
