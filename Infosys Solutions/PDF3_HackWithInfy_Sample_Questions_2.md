# HackWithInfy Sample Questions - 2

## 1. Easy: Range AP Update & Sum Queries

### Problem Description
You are given an array $A$ of $n$ integers and $q$ queries. Each query can be one of the following two types:
- **Type 1 Query (1, l, r):** Replace $A[i]$ with $(i - l + 1) \cdot A[l]$ for each index $i$ where $l \le i \le r$.
- **Type 2 Query (2, l, r):** Calculate the sum of the elements in $A$ from index $l$ to index $r$.

Find the sum of answers to all Type 2 queries modulo $10^9+7$.

### Input Format
- The first line contains an integer, $n$, denoting the number of elements in $A$.
- Each line $i$ of the $n$ subsequent lines (where $0 \le i < n$) contains an integer describing $A[i]$.
- The next line contains an integer, $q$, denoting the number of queries.
- Each line $i$ of the $q$ subsequent lines (where $0 \le i < q$) contains 3 space-separated integers describing `queries[i]`. The 3 space-separated integers denote the value of either $(1, l, r)$ or $(2, l, r)$.

### Constraints
- $1 \le n \le 10^5$
- $1 \le A[i] \le 10^5$
- $1 \le q \le 10^5$
- $0 \le l \le r < n$

---

### Sample Test Cases

#### Case 1
**Input:**
```text
7
1
4
5
1
6
7
8
5
1 1 6
1 1 5
2 5 5
2 3 4
2 3 3
```
**Output:**
```text
60
```
**Explanation:**
Here, $n = 7$, $A = [1, 4, 5, 1, 6, 7, 8]$, $q = 5$.
- **Query 1 (1, 1, 6):** Replaces $A[i]$ with $(i - 1 + 1) \cdot A[1]$ for $1 \le i \le 6$.
  - $A[1] = 4$
  - $A$ becomes $[1, 4, 8, 12, 16, 20, 24]$
- **Query 2 (1, 1, 5):** Replaces $A[i]$ with $(i - 1 + 1) \cdot A[1]$ for $1 \le i \le 5$.
  - $A$ remains $[1, 4, 8, 12, 16, 20, 24]$
- **Query 3 (2, 5, 5):** Sum from index 5 to 5 is $A[5] = 20$.
- **Query 4 (2, 3, 4):** Sum from index 3 to 4 is $A[3] + A[4] = 12 + 16 = 28$.
- **Query 5 (2, 3, 3):** Sum from index 3 to 3 is $A[3] = 12$.
- **Total Answer:** $20 + 28 + 12 = 60$.

---

## 2. Easy: Max Sum of Good Subarray

### Problem Description
You are given an array $A$ of length $N$ and an integer $k$.
A subarray from $l$ to $r$ is considered **good** if the number of distinct elements in that subarray does not exceed $k$. Additionally, an empty subarray is also a good subarray, and its sum is considered to be zero.

Find the maximum sum of a good subarray.

### Input Format
- The first line contains an integer, $N$, denoting the number of elements in $A$.
- The next line contains an integer, $k$, denoting the limit on the distinct elements.
- Each line $i$ of the $N$ subsequent lines (where $0 \le i < N$) contains an integer describing $A[i]$.

### Constraints
- $1 \le N \le 10^5$
- $1 \le k \le N$
- $-10^5 \le A[i] \le 10^5$

---

### Sample Test Cases

#### Case 1
**Input:**
```text
11
2
1
2
2
3
2
3
5
1
2
1
1
```
**Output:**
```text
12
```
**Explanation:**
We can select the subarray $[2, 2, 3, 2, 3]$ (from index 2 to 6). It contains at most 2 distinct elements ($2$ and $3$). Its sum is $2 + 2 + 3 + 2 + 3 = 12$.

#### Case 2
**Input:**
```text
3
1
-1
-2
-3
```
**Output:**
```text
0
```
**Explanation:**
Since all elements are negative, it is optimal to choose the empty subarray, yielding a sum of 0.

---

## 3. Easy: Oil Tank Disturbances

### Problem Description
You have an oil tank with a capacity of $C$ litres that can be bought and sold by $N$ people. The people standing in a queue are served sequentially in the order of array $A$.

Some of them want to sell a litre of oil and some of them want to buy a litre of oil. $A[i] = 1$ denotes that the $i$-th person wants to sell a litre of oil, and $A[i] = -1$ denotes that they want to buy a litre of oil.

When a person wants to sell a litre of oil but the tank is full, they cannot sell it and become upset. Similarly, when a person wants to buy a litre of oil but the tank is empty, they cannot buy it and become upset. Both these cases cause disturbances.

Find the minimum initial amount of oil $X$ ($0 \le X \le C$) that results in the least number of disturbances. If there are multiple values of $X$ that yield the same minimum number of disturbances, output the minimum such $X$.

### Input Format
- The first line contains an integer, $N$, denoting the number of people.
- The next line contains an integer, $C$, denoting the capacity of the tank.
- Each line $i$ of the $N$ subsequent lines contains an integer describing $A[i]$.

### Constraints
- $1 \le N \le 10^5$
- $1 \le C \le 10^5$
- $-1 \le A[i] \le 1$ ($A[i] \in \{-1, 1\}$)

---

### Sample Test Cases

#### Case 1
**Input:**
```text
3
3
-1
1
1
```
**Output:**
```text
1
```
**Explanation:**
- If $X = 1$:
  - Person 1 buys 1L. Tank becomes 0L. No disturbance.
  - Person 2 sells 1L. Tank becomes 1L. No disturbance.
  - Person 3 sells 1L. Tank becomes 2L. No disturbance.
  - Total disturbances = 0.
- Minimum initial amount $X$ to achieve 0 disturbances is 1 litre.

---

## 4. Easy: Army Reduction Game

### Problem Description
General Ali has devised a strategic game to reduce an enemy army of $N$ soldiers to just 1 soldier using a minimal number of moves.

The game allows the following three types of moves:
1. Reduce the enemy army by 1 soldier.
2. Reduce the enemy army by half of its current soldiers, rounding down to the nearest integer. (i.e., $N \to N - \lfloor N/2 \rfloor = \lceil N/2 \rceil$).
3. Reduce the enemy army by two-thirds of its current soldiers, rounding down to the nearest integer. (i.e., $N \to N - \lfloor 2N/3 \rfloor = \lceil N/3 \rceil$).

Each move must ensure that the resulting number of soldiers is an integer. Find the minimum number of moves required to reduce the enemy army to just 1 soldier.

### Input Format
- The first line contains an integer, $N$, denoting the number of enemy soldiers.

### Constraints
- $1 \le N \le 10^9$

---

### Sample Test Cases

#### Case 1
**Input:**
```text
5
```
**Output:**
```text
3
```
**Explanation:**
- Move 1: Reduce by half ($5 \to 3$). (Wait, $5 - \lfloor 5/2 \rfloor = 3$).
- Move 2: Reduce by half ($3 \to 2$). ($3 - \lfloor 3/2 \rfloor = 2$).
- Move 3: Reduce by half ($2 \to 1$). ($2 - \lfloor 2/2 \rfloor = 1$).
Minimum moves = 3.

---

## 5. Easy: Grid Invasion

### Problem Description
General Ali has initiated an invasion in the shape of an $N \times M$ grid behind enemy lines given by a 2D array $Q$.
The grid consists of cells represented by the following characters:
- `*`: Represents a block cell that cannot be visited.
- `A`: Represents a cell that has been invaded by General Ali's army.
- `E`: Represents a cell that contains the enemy's army.

General Ali's invasion progresses as follows: At each second, any cell marked `E` that shares a side with a cell marked `A` is invaded by General Ali's army (becomes `A`).

Find the minimum time it will take for General Ali's army to invade all enemy cells (`E`) in the grid. If it's not possible to invade all enemy cells, return $-1$.

### Input Format
- The first line contains an integer, $N$, denoting the number of rows.
- The next line contains an integer, $M$, denoting the number of columns.
- Each line $i$ of the $N$ subsequent lines contains a string of length $M$ describing the $i$-th row.

### Constraints
- $1 \le N, M \le 10^3$
- The string contains only `*`, `A`, and `E`.

---

### Sample Test Cases

#### Case 1
**Input:**
```text
2
2
AE
EE
```
**Output:**
```text
2
```
**Explanation:**
- After 1 second: `Q = [["AA"], ["AE"]]`
- After 2 seconds: `Q = [["AA"], ["AA"]]`
Minimum time = 2.

---

## 6. Medium: Max Expert Number (MEX Partitions)

### Problem Description
A company ABC has $N$ employees.
- Each employee $i$ works on the $i$-th floor and has skill $A[i]$.
- Each employee can belong to at most one team.
- Each team should have employees working on consecutive floors from $i$ to $j$. In other words, the teams should be divided in such a way that no employee of one team can walk into the project space of another team. (This means teams are disjoint contiguous subarrays of $A$).
- ABC uses a metric called the **expert number** which is calculated as the sum of all the absent expert values from each team of employees. The absent expert value of each team is the first skill starting from 0 which is not present in the team (i.e., the MEX of the team's skills).

Find the maximum expert number that can be obtained.

### Input Format
- The first line contains an integer, $N$, denoting the number of employees.
- Each line $i$ of the $N$ subsequent lines contains an integer describing $A[i]$.

### Constraints
- $1 \le N \le 10^5$
- $0 \le A[i] \le 10^3$

---

### Sample Test Cases

#### Case 1
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

## 7. Medium: Graph Component Beauty

### Problem Description
You are given a graph with $n$ nodes. Initially, the graph is disconnected, meaning it contains zero edges.
Each node has a value written on it such that the $i$-th node has a value $i$ (1-indexed).

We say that a range $[l, r]$ is covered in a set $S$, if for each $i$ from $l$ to $r$, $i$ appears in $S$.
Now, let's define `beauty(S)` as the minimum number of covered ranges such that each element of $S$ belongs to at least one of these ranges. For example: `beauty([1, 2, 4, 5, 8, 11]) = 4` (ranges are $[1, 2], [4, 5], [8], [11]$).

You have to process $q$ queries that are either of the following types:
- **Type 1 (1, u, v):** Add an undirected edge between $u$ and $v$.
- **Type 2 (2, u, 0):** Find the number of covered ranges in the connected component of $u$. (i.e. `beauty(connected_component(u))`).

Find the sum of answers to all Type 2 queries.

### Input Format
- The first line contains an integer, $n$, denoting the size of the graph.
- The next line contains an integer, $q$, denoting the number of queries.
- The next line contains an integer, $t$, denoting the number of columns in queries (usually 3).
- Each line $i$ of the $q$ subsequent lines contains $t$ space-separated integers describing `queries[i]`.

### Constraints
- $1 \le n, q \le 10^5$
- $t = 3$
- $0 \le queries[i][j] \le n$

---

### Sample Test Cases

#### Case 1
**Input:**
```text
2
1
3
2 1 0
```
**Output:**
```text
1
```
**Explanation:**
Initially disconnected. Component of 1 is $\{1\}$. `beauty({1}) = 1` ($[1, 1]$).

---

## 8. Medium: BFS on Circular Jumps

### Problem Description
A group of $N$ people are seated around a circular table to play a game.
The game involves jumping from one chair to another. Each person sitting on chair $i$ can jump $A[i]$ chairs to either the right or left in one jump, where $1 \le i \le N$.

Bob, sitting on chair $X$, needs to reach chair $Y$, where the escape door is located.
Find the minimum number of jumps required to reach chair $Y$ from chair $X$. If this is impossible using the given jump distances, then return $-1$.

### Input Format
- The first line contains an integer, $N$, denoting the number of chairs.
- The next line contains an integer, $X$, denoting Bob's starting chair (1-indexed).
- The next line contains an integer, $Y$, denoting Bob's target chair.
- Each line $i$ of the $N$ subsequent lines contains an integer $A[i]$.

### Constraints
- $1 \le N \le 10^5$
- $1 \le X, Y \le N$
- $1 \le A[i] \le 10^5$

---

### Sample Test Cases

#### Case 1
**Input:**
```text
5
5
1
1
2
3
2
4
```
**Output:**
```text
1
```
**Explanation:**
Bob starts at chair 5. From chair 5, he can jump $A[5] = 4$ positions left or right.
Right jump from 5: $(5 + 4 - 1) \pmod 5 + 1 = 4$.
Left jump from 5: $(5 - 4 - 1) \pmod 5 + 1 = 1$.
Bob can reach chair 1 in 1 jump.

---

## 9. Medium: Great Chain Probability

### Problem Description
You are given two boxes: one contains an infinite number of blue balls, and the other contains an infinite number of red balls. We can construct a chain of balls of length $N$ by choosing a box, taking a ball, and inserting it at the end of the chain.

A chain is called **good** if at any point in the chain, the number of blue balls does not exceed the number of red balls by more than $K$. That is, if after adding the $i$-th ball we have $B[i]$ blue balls and $R[i]$ red balls, then $B[i] \le R[i] + K$.

A chain is called **great** if it is a good chain and, if we take the reversed chain, the following matching conditions satisfy:
- Every blue ball in the reversed chain is matched with a red ball in the original chain.
- Every red ball in the reversed chain is matched with a blue ball in the original chain.

You are given two integers $B$ and $R$. Let the probability of choosing the box with the blue balls be $B / 10^6$ and the probability of choosing the box with red balls be $R / 10^6$.

Find the probability of creating a great chain of length $N$. Since the answer can be large, return it modulo $10^9+7$.

### Input Format
- The first line contains an integer, $N$, denoting the length of the chain.
- The next line contains an integer, $K$.
- The next line contains $B$.
- The next line contains $R$.

### Constraints
- $1 \le N \le 10^9$
- $1 \le K \le 100$
- $1 \le B, R \le 10^6$

---

### Sample Test Cases

#### Case 1
**Input:**
```text
1
1
199252
470888
```
**Output:**
```text
542964004
```
**Explanation:**
The output is the probability modulo $10^9+7$.

---

## 10. Medium: Max Subarray XOR Sum

### Problem Description
You are given an array $A$ of size $N$.
You can partition $A$ into multiple contiguous subarrays such that each element belongs to exactly one subarray, and each subarray has a length of at least $K$.

The beauty of a subarray is the maximum bitwise XOR of a subset of elements in that subarray. The amazingness of a partitioned array is the sum of beauties of its subarrays.

Find the maximum possible amazingness of $A$.

### Input Format
- The first line contains an integer, $N$, denoting the number of elements in $A$.
- The next line contains an integer, $K$, denoting the minimum length of each subarray.
- Each line $i$ of the $N$ subsequent lines contains $A[i]$.

### Constraints
- $1 \le N \le 10^5$
- $1 \le K \le 10^5$
- $1 \le A[i] \le 10^5$

---

### Sample Test Cases

#### Case 1
**Input:**
```text
2
2
2
1
```
**Output:**
```text
3
```
**Explanation:**
We partition $A$ into one subarray $[2, 1]$. The maximum XOR of a subset is $2 \oplus 1 = 3$.

---

## 11. Hard: Min K for Path Length

### Problem Description
You are given a permutation $p$ of length $n$ and an integer $m$. You now need to construct a directed graph from the given permutation.
An edge exists from $i$ to $j$ if $p[i] < p[j]$ and $|i - j| \le k$.

Find the minimum value of $k$ such that the longest path of the resulting graph is greater than or equal to $m$. (The length of the path is equal to the number of nodes in that path).

### Input Format
- The first line contains an integer, $n$, denoting the number of elements in $p$.
- The next line contains $m$.
- Each line $i$ of the $n$ subsequent lines contains $p[i]$.

### Constraints
- $1 \le n \le 10^5$
- $1 \le m \le n$
- $1 \le p[i] \le n$

---

### Sample Test Cases

#### Case 1
**Input:**
```text
5
2
1
3
2
5
4
```
**Output:**
```text
1
```
**Explanation:**
$p = [1, 3, 2, 5, 4]$ and $m = 2$.
If $k \ge 1$, edge $1 \to 2$ exists (since $p[1] = 3 < p[2] = 2$ is false, wait, 1-indexed?
Wait, if $p = [1, 3, 2, 5, 4]$, then:
$p[0] = 1, p[1] = 3, p[2] = 2, p[3] = 5, p[4] = 4$.
If $k = 1$:
$p[0] = 1 < p[1] = 3$ and $|0-1| = 1 \le 1$. Directed edge $0 \to 1$ exists.
The path $0 \to 1$ has 2 nodes. So longest path is 2, which is $\ge m = 2$.
So minimum $k$ is 1.

---

## 12. Hard: Soldiers & Treasure Chests

### Problem Description
There are $N$ soldiers, where $N$ is an even number. There are also $N$ treasure chests, each with a bonus value given by the array `Bonus`.

The power of each soldier is described by an array $A$ of size $N$. For each $i$, the power of the $i$-th soldier is an integer between $1$ and $N/2$, and each number between $1$ and $N/2$ occurs exactly twice in $A$.

The game has $N$ rounds, and each round $i$ ($1 \le i \le N$) proceeds as follows:
1. Bob finds the first player $R$ on the right ($R > i$) whose power is a multiple of the power of the $i$-th player.
2. If no such player $R$ is found, Bob does nothing.
3. If such a player $R$ is found, Bob can choose any chest in the range $[i, R]$ that gives the maximum bonus. Let's call the bonus of this chest $X$.
4. The total XP is increased by $X$.

Find the total XP that Bob can obtain from all $N$ rounds. (Each chest can be used any number of times).

### Input Format
- The first line contains an integer, $N$, denoting the number of elements in $A$.
- Each line $i$ of the $N$ subsequent lines contains $A[i]$.
- Each line $i$ of the $N$ subsequent lines contains $Bonus[i]$.

### Constraints
- $1 \le N \le 10^5$
- $1 \le A[i] \le N/2$
- $1 \le Bonus[i] \le 10^5$

---

### Sample Test Cases

#### Case 1
**Input:**
```text
4
1
1
2
2
4
8
2
1
```
**Output:**
```text
18
```
**Explanation:**
$A = [1, 1, 2, 2]$, $Bonus = [4, 8, 2, 1]$.
- Round 1 (soldier 1, power 1): First soldier on right with multiple of 1 is soldier 2 (power 1). Range $[1, 2]$. Max bonus is $\max(4, 8) = 8$.
- Round 2 (soldier 2, power 1): First on right with multiple of 1 is soldier 3 (power 2). Range $[2, 3]$. Max bonus is $\max(8, 2) = 8$.
- Round 3 (soldier 3, power 2): First on right with multiple of 2 is soldier 4 (power 2). Range $[3, 4]$. Max bonus is $\max(2, 1) = 2$.
- Round 4 (soldier 4, power 2): No soldier on right.
Total XP = $8 + 8 + 2 = 18$.

---

## 13. Hard: Distinct Frequency Pairs

### Problem Description
You are given an array $A$ of length $N$.
We define two functions:
- `frequency(left, right, value)`: Returns the number of elements in the range $[left, right]$ equal to `value`.
- `distinct(left, right)`: Returns the number of distinct elements in the range $[left, right]$.

Find the number of pairs $(i, j)$ with $1 \le i < j \le N$ that satisfy the following condition:
$$\text{frequency}(1, i, A[i]) + \text{frequency}(j, N, A[j]) \le \lfloor \text{distinct}(1, i) / 2 \rfloor + \lfloor \text{distinct}(j, N) / 2 \rfloor$$

Return the answer modulo $10^9+7$.

### Input Format
- The first line contains an integer, $N$, denoting the number of elements in $A$.
- Each line $i$ of the $N$ subsequent lines contains $A[i]$.

### Constraints
- $1 \le N \le 10^5$
- $1 \le A[i] \le 10^9$

---

### Sample Test Cases

#### Case 1
**Input:**
```text
5
2
2
3
1
5
```
**Output:**
```text
2
```
**Explanation:**
$A = [2, 2, 3, 1, 5]$. We can select two pairs $(1, 2)$ and $(3, 4)$ (1-indexed? Wait, $1 \le i < j \le N$) which satisfy the conditions.

---

## 14. Hard: Tree Rooted Subtree Intersection

### Problem Description
You are given a tree consisting of $N$ nodes. You are also given two distinct nodes $A$ and $B$.
You are given an array $P$ where the parent of node $u$ is given by $P[u]$.

We define the beauty of a node pair $(U, V)$ as the number of nodes that belong to both:
- The subtree of $U$ when the tree is rooted at $A$.
- The subtree of $V$ when the tree is rooted at $B$.

You are given $Q$ queries. For each query, you are given two nodes $U$ and $V$.
Let $K$ be the answer to the last query (initially 0). The query values $U$ and $V$ are updated as:
- $U' = (U + K) \pmod N + 1$
- $V' = (V + K) \pmod N + 1$

Find the sum of answers to all queries modulo $10^9+7$.

### Input Format
- The first line contains $N$.
- The next line contains $A$.
- The next line contains $B$.
- The next $N$ lines each contain $P[i]$ (parent of node $i$).
- The next line contains $Q$.
- The next line contains $Col$ (number of columns in queries, always 2).
- The next $Q$ lines each contain two space-separated integers describing the query.

### Constraints
- $1 \le N, Q \le 10^5$
- $1 \le A, B \le N$
- $0 \le P[i] \le N$
