# Food Stamps Explainer

## Problem Description & Example Test Case
You have $N$ types of food. You can buy any type of food any number of times, up to $M$ total meals.
Buying the $i$-th type of food for the $t_i$-th time gives $v[i] - d[i] \cdot (t_i - 1)$ taste points.
Find the maximum taste points you can achieve.

### Example Test Case
Input: $N=2, M=2, v=[5, 7], d=[2, 4]$.
Output: 12 (buy first food once (5) and second food once (7)).

---

## Prerequisite Concepts
- **Greedy Choice:** Always select the local maximum value.
- **Simulation:** Simulating the process of buying meals one by one.

---

## The Chosen Approach (Naive)
We simulate the process of buying $M$ meals one by one. At each step:
1. We scan the list of food types to find the one that currently yields the maximum taste value.
2. We add this value to our total taste points.
3. We decrement the taste value of this food type by its decay factor $d[i]$.
We repeat this process $M$ times, or until all food types have a non-positive taste value.

---

## Complexity Breakdown
- **Time Complexity:** $O(M \cdot N)$
- **Space Complexity:** $O(1)$

---

## Pseudocode
```text
total_taste = 0
repeat M times:
    best_idx = index of max(v)
    if v[best_idx] <= 0:
        break
    total_taste += v[best_idx]
    v[best_idx] -= d[best_idx]
return total_taste
```
