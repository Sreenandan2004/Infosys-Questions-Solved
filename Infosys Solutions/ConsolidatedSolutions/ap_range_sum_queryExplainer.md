# AP Range Sum Query Explainer

## Problem Description & Example Test Case
You are given an array $A$ of $n$ integers and $q$ queries:
- **Type 1 Query (1, l, r):** Replace $A[i]$ with $(i - l + 1) \cdot A[l]$ for each index $i$ where $l \le i \le r$.
- **Type 2 Query (2, l, r):** Calculate the sum of the elements in $A$ from index $l$ to index $r$.

Find the sum of answers to all Type 2 queries modulo $10^9+7$.

### Example Test Case
Input: $n=7, A=[1, 4, 5, 1, 6, 7, 8]$, queries = `[[1, 1, 6], [2, 3, 4]]`.
Output: $28$.

---

## Prerequisite Concepts
- **Array Traversal:** Loops to perform element-wise range assignments and range sums.

---

## The Chosen Approach (Naive)
We process each of the $Q$ queries sequentially:
- For Type 1: We first lookup the current value of $A[l]$. Then, we loop $i$ from $l$ to $r$ and assign $A[i] = (i - l + 1) \cdot A[l]$.
- For Type 2: We loop $i$ from $l$ to $r$ and compute the sum of $A[i]$ modulo $10^9+7$, and add it to our running answer sum.

---

## Complexity Breakdown
- **Time Complexity:** $O(Q \cdot N)$
- **Space Complexity:** $O(1)$

---

## Pseudocode
```text
ans_sum = 0
for each query (type, l, r):
    if type == 1:
        val = A[l]
        for i from l to r:
            A[i] = (i - l + 1) * val
    else:
        curr_sum = 0
        for i from l to r:
            curr_sum = (curr_sum + A[i]) % MOD
        ans_sum = (ans_sum + curr_sum) % MOD
return ans_sum
```
