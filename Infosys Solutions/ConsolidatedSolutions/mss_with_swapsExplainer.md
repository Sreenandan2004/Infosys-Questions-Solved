# MSS with Swaps Explainer

## Problem Description & Example Test Case
Given an array $a$ of length $n$ and an integer $k$. You must perform exactly $k$ swaps of elements in the array.
Find the maximum possible Maximum Subarray Sum (MSS) after performing the swaps.

### Example Test Case
Input: $n=3, k=1, a=[1, 2, -5]$.
Output: 3 (swap 1 and -5 to get $[-5, 2, 1]$, sum of $[2, 1]$ is 3).

---

## Prerequisite Concepts
- **Maximum Subarray Sum:** Finding the contiguous subarray with the largest sum.
- **Greedy Strategy:** Replacing the smallest elements in a subarray with the largest elements from outside.

---

## The Naive Approach
A complete backtracking search of all possible swaps, then running Kadane's algorithm on each.
- **Time Complexity:** $O(N^{2k} \cdot N)$
- **Space Complexity:** $O(N)$

---

## The Optimal Approach
For any candidate subarray $A[l..r]$:
To maximize its sum, we should replace its smallest elements (that are negative or small) with the largest elements from outside the subarray. We can do at most $k$ swaps.
Thus, we sort the elements inside the subarray in ascending order, and the elements outside in descending order.
Then we pair them up: if an outside element is larger than an inside element, we swap them.
For $N \le 500$, we can iterate over all $O(N^2)$ subarrays and greedily perform the swaps.

---

## Optimal Complexity Breakdown
- **Time Complexity:** $O(N^3 \log N)$ (or $O(N^2 \cdot k)$ using optimized heap tracking)
- **Space Complexity:** $O(N)$

---

## Pseudocode
```text
ans = -infinity
for l from 0 to n-1:
    for r from l to n-1:
        inside = a[l..r]
        outside = a[0..l-1] + a[r+1..n-1]
        sort(inside, ascending)
        sort(outside, descending)
        sum = sum(inside)
        for i from 0 to min(k, len(inside), len(outside))-1:
            if outside[i] > inside[i]:
                sum += outside[i] - inside[i]
        ans = max(ans, sum)
```
