# Arithmetic Progression Range Query Explainer

## Problem Description & Example Test Case
You have an array $A$ of integers with $n$ elements. There are $q$ queries to process.
For the subarray of $A$ ranging from index $l$ to $r$, assign a sequence of integers starting from $x$ and increasing by $y$. This means:
- $A[l + i] = x + i \cdot y$, where $i$ ranges from $0$ to $r - l$.

Find the sum of all integers in $A$ after processing all queries. Return it modulo $10^9+7$.

### Example Test Case
Input:
$A = [5, 5, 0, 3, 0]$
Query: $l=0, r=2, x=1, y=2 \implies A[0]=1, A[1]=3, A[2]=5$.
Output: $51$ (after all 5 queries).

---

## Prerequisite Concepts
- **Array Traversal:** Directly modifying elements in a contiguous index range.
- **Arithmetic Progressions:** The formula $x + (i - l) \cdot y$ determines the value at each index.

---

## The Chosen Approach (Naive)
Since the complexity of $O(Q \cdot N)$ is acceptable for easy category inputs, we loop over each query and directly update the elements of the array $A$ in the range $[l, r]$.
At the end of all queries, we compute the sum of the array elements modulo $10^9+7$.

---

## Complexity Breakdown
- **Time Complexity:** $O(Q \cdot N)$
- **Space Complexity:** $O(1)$ (in-place modification of the array)

---

## Pseudocode
```text
for each query (l, r, x, y):
    for i from l to r:
        A[i] = x + (i - l) * y
return sum(A) % MOD
```
