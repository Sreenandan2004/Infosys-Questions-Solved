# Great Chain Probability Explainer

## Problem Description & Example Test Case
You pick blue (B) balls with weight $B$ and red (R) balls with weight $R$ to form a chain of length $N$.
- A chain is good if at any prefix, $B_{count} \le R_{count} + K$.
- A chain is great if it is good and satisfies reversed matching conditions.
Find the probability of generating a great chain modulo $10^9+7$.

### Example Test Case
Input: $N=2, K=1, B=748096, R=475634$.
Output: $170882874$.

---

## Prerequisite Concepts
- **Random Walks:** Modeling sequence states as position movement on a grid.
- **Matrix Exponentiation:** Multiplying transition matrices in $O(\log N)$ time.

---

## The Naive Approach
Evaluate all $2^N$ possible strings, check if they are great, and sum their probabilities.
- **Time Complexity:** $O(2^N)$
- **Space Complexity:** $O(N)$

---

## The Optimal Approach
The problem reduces to a random walk where picking B is $+1$ and R is $-1$. The prefix sums $S_i$ (difference between count of B and R) must stay within $[0, K]$ at all times.
We can model this as a Markov chain with $K+1$ states. The transition matrix $M$ is:
- $M[j+1][j] = p$ (transition from $j$ to $j+1$ with probability of B)
- $M[j-1][j] = q$ (transition from $j$ to $j-1$ with probability of R)
We compute $M^N$ using matrix exponentiation. The sum of the first column of $M^N$ gives the probability of starting at 0 and staying within $[0, K]$ for $N$ steps.

---

## Optimal Complexity Breakdown
- **Time Complexity:** $O(K^3 \log N)$
- **Space Complexity:** $O(K^2)$

---

## Pseudocode
```text
size = K + 1
M = matrix of size size x size
for j from 0 to K:
    if j + 1 <= K: M[j+1][j] = p
    if j - 1 >= 0: M[j-1][j] = q
    
M_N = matrix_power(M, N)
ans = sum(M_N[i][0] for i from 0 to K)
```
