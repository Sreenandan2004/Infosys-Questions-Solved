# Oil Tank Disturbances Explainer

## Problem Description & Example Test Case
You have an oil tank of capacity $C$ and $N$ transactions: $A[i] = 1$ (sell 1L), $A[i] = -1$ (buy 1L).
- Selling to a full tank causes a disturbance.
- Buying from an empty tank causes a disturbance.
Find the initial amount of oil $X \in [0, C]$ that minimizes disturbances. (Choose the minimum $X$ in case of ties).

### Example Test Case
Input: $N=3, C=3, A=[-1, 1, 1]$.
Output: 1 (initial oil 1 gives 0 disturbances).

---

## Prerequisite Concepts
- **Simulation:** Simulating the state transitions of the oil level step by step.

---

## The Chosen Approach (Naive)
We directly test all possible initial oil values $X$ in the range $[0, C]$:
1. For each candidate $X$, we simulate the $N$ transactions and count the total number of disturbances.
2. We keep track of the value of $X$ that yields the minimum number of disturbances.
3. If there is a tie, we naturally pick the smaller $X$ since we iterate $X$ from $0$ up to $C$.

---

## Complexity Breakdown
- **Time Complexity:** $O(C \cdot N)$
- **Space Complexity:** $O(1)$

---

## Pseudocode
```text
min_dist = infinity
best_x = -1
for x from 0 to C:
    dist = get_dist_for_initial_oil(x)
    if dist < min_dist:
        min_dist = dist
        best_x = x
return best_x
```
