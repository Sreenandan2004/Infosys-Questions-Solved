# Max Sum of Good Subarray Explainer

## Problem Description & Example Test Case
Given an array $A$ of length $N$ and an integer $k$. A subarray is **good** if the number of distinct elements in it does not exceed $k$. An empty subarray has sum 0.
Find the maximum sum of a good subarray.

### Example Test Case
Input: $N=11, k=2, A=[1, 2, 2, 3, 2, 3, 5, 1, 2, 1, 1]$.
Output: 12 (subarray $[2, 2, 3, 2, 3]$).

---

## Prerequisite Concepts
- **Subarray Generation:** Generating all contiguous parts of an array using nested loops.
- **Set Data Structure:** To track the number of distinct elements.

---

## The Chosen Approach (Naive)
We generate all possible subarrays $A[l..r]$ using nested loops.
- For each starting position $l$, we expand the subarray to the right by incrementing $r$.
- We maintain a set of seen elements in the current subarray. If the size of the set is $\le k$, it is a valid "good" subarray, and we check if its sum is the maximum seen so far.
- If the size of the set exceeds $k$, any further extension will also have $> k$ distinct elements, so we break and move to the next starting position $l$.

---

## Complexity Breakdown
- **Time Complexity:** $O(N^2)$
- **Space Complexity:** $O(N)$ (to store distinct elements in the set)

---

## Pseudocode
```text
ans = 0
for l from 0 to n-1:
    distinct = empty set
    curr_sum = 0
    for r from l to n-1:
        distinct.add(A[r])
        curr_sum += A[r]
        if len(distinct) <= k:
            ans = max(ans, curr_sum)
        else:
            break
return ans
```
