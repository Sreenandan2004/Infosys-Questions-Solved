# Sum Maximization Explainer

## Problem Description & Example Test Case
You have two arrays $A$ and $B$ of length $N$, and variables $X, Y, Z$. In each $i$-th operation:
1. Subtract $B[i]$ from sum.
2. Decrease both $X$ and $Y$ by 1, then add $A[i] \cdot X \cdot Y \cdot Z$ to sum.
3. Decrease both $Y$ and $Z$ by 1, then add $A[i] \cdot X \cdot Y \cdot Z$ to sum.
All $X, Y, Z$ must remain $\ge 0$. Find the maximum sum modulo $10^9+7$.

### Example Test Case
Input: $N=2, X=1, Y=2, Z=2$, $A=[0,0], B=[10,5]$
Output: 0.

---

## Prerequisite Concepts
- **Dynamic Programming (DP):** Tracking state changes to compute the optimal strategy.

---

## The Naive Approach
A backtracking search that branches on the 3 options for each of the $N$ steps.
- **Time Complexity:** $O(3^N)$
- **Space Complexity:** $O(N)$

---

## The Optimal Approach
At step $i$, let $c_2$ be the count of type 2 operations and $c_3$ be the count of type 3 operations.
The current values of the variables are uniquely determined by:
- $X_{curr} = X - c_2$
- $Y_{curr} = Y - c_2 - c_3$
- $Z_{curr} = Z - c_3$
Since $c_2 + c_3 \le i$, we can define a DP table where `dp[(c2, c3)]` stores the maximum sum. At each step $i$, we transition to $i+1$ using the three operational choices, updating the DP state.

---

## Optimal Complexity Breakdown
- **Time Complexity:** $O(N \cdot X \cdot Z)$ (which is at most $O(N^3)$)
- **Space Complexity:** $O(X \cdot Z)$

---

## Pseudocode
```text
dp = {(0, 0): 0}
for i from 0 to n-1:
    new_dp = {}
    for each (c2, c3) in dp:
        # Op 1
        new_dp[(c2, c3)] = max(new_dp[(c2, c3)], dp[(c2, c3)] - B[i])
        # Op 2
        if X - c2 - 1 >= 0 and Y - c2 - c3 - 1 >= 0:
            new_dp[(c2+1, c3)] = max(..., dp[(c2, c3)] + A[i]*(X-c2-1)*(Y-c2-c3-1)*(Z-c3))
        # Op 3
        if Y - c2 - c3 - 1 >= 0 and Z - c3 - 1 >= 0:
            new_dp[(c2, c3+1)] = max(..., dp[(c2, c3)] + A[i]*(X-c2)*(Y-c2-c3-1)*(Z-c3-1))
    dp = new_dp
```
