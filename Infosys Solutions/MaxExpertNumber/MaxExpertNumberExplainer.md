# Max Expert Number Explainer

## Problem Description & Example Test Case
A company ABC has $N$ employees.
- Each employee $i$ works on the $i$-th floor and has skill $A[i]$.
- Each employee can belong to at most one team.
- Each team should have employees working on consecutive floors from $i$ to $j$. (This means teams are disjoint contiguous subarrays of $A$).
- ABC uses a metric called the **expert number** which is calculated as the sum of all the absent expert values from each team of employees. The absent expert value of each team is the first skill starting from 0 which is not present in the team (i.e., the MEX of the team's skills).

Find the maximum expert number that can be obtained.

### Example Test Case
**Input:**
```text
4
0
2
1
1
```
**Output:**
```text
3
```
**Explanation:**
We can divide the employees into the following teams: $[0, 2, 1]$, $[1]$.
- Team 1: $[0, 2, 1]$. MEX is 3.
- Team 2: $[1]$. MEX is 0.
- Total expert number = $3 + 0 = 3$.

---

## Prerequisite Concepts
- **Dynamic Programming (Partition DP):** Partitioning an array to maximize a sum of values.
- **MEX (Minimum Excludant):** The smallest non-negative integer not present in a set.

---

## The Naive Approach
A naive DP would define $dp[i]$ as the maximum expert number for the prefix $A[0..i-1]$.
$$dp[i] = \max_{0 \le j < i} (dp[j] + \text{MEX}(A[j..i-1]))$$
For $N \le 10^5$, calculating this naively takes $O(N^2)$ transitions, which is too slow.
- **Time Complexity:** $O(N^2)$
- **Space Complexity:** $O(N)$

---

## Guided Discovery (The Optimal Approach)
Let's observe the constraints:
- $0 \le A[i] \le 10^3$.
- This means the maximum possible MEX of any team is at most $\max(A) + 1 \le 1001$.
- Let $M$ be the target MEX value. To get a MEX of at least $M$, our team subarray $A[j..i-1]$ must contain all elements $0, 1, 2, \dots, M-1$.

For a fixed ending floor $i-1$, what is the largest starting floor $j$ such that $A[j..i-1]$ contains all of $0, 1, \dots, M-1$?
It must be the minimum of the last occurrence positions of all numbers $0, 1, \dots, M-1$ before or at index $i-1$. Let's call this position `min_last[M]`.

If we want to achieve a MEX of at least $M$, the starting floor $j$ can be at most `min_last[M]`.
Since $dp[j]$ is non-decreasing with $j$ (we can always choose not to include elements, so having a larger prefix never hurts), to maximize $dp[j] + M$ for a fixed $M$, we should greedily pick the largest valid $j$, which is exactly $j = \text{min\_last}[M]$!

Thus, the DP transition becomes:
$$dp[i] = \max \left( dp[i-1], \max_{1 \le M \le 1002} (dp[\text{min\_last}[M]] + M) \right)$$

For each element $A[i-1]$:
1. Update `last_pos[A[i-1]] = i-1`.
2. Compute `min_last[M] = min(min_last[M-1], last_pos[M-1])` for $M = 1 \dots 1002$.
3. Compute $dp[i]$ in $O(\max(A))$ time.

This reduces the complexity from $O(N^2)$ to $O(N \cdot \max(A))$!

---

## Visualizations
The DP state transition at index $i$ depends on the last occurrence positions of numbers:

```mermaid
graph TD
    A[Current element A[i-1]] --> B[Update last_pos]
    B --> C[Compute min_last for each M from 1 to 1002]
    C --> D[DP Transition: max of dp[i-1] and dp[min_last[M]] + M]
    D --> E[dp[i]]
```

---

## Optimal Complexity Breakdown
- **Time Complexity:** $O(N \cdot \max(A))$ where $\max(A) \le 1000$.
- **Space Complexity:** $O(N + \max(A))$ to store the DP array and occurrence indices.

---

## Pseudocode
```text
dp = array of size N+1 initialized to 0
last_pos = array of size 1005 initialized to -1
min_last = array of size 1005 initialized to -1

for i from 1 to N:
    last_pos[A[i-1]] = i-1
    min_last[0] = i-1
    dp[i] = dp[i-1]
    
    for M from 1 to 1002:
        min_last[M] = min(min_last[M-1], last_pos[M-1])
        if min_last[M] >= 0:
            dp[i] = max(dp[i], dp[min_last[M]] + M)
```
