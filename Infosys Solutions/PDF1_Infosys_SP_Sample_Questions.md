# Infosys SP Sample Questions

## Sample 1: Easy (Arithmetic Progression Range Queries)

### Problem Description
You have an array $A$ of integers with $n$ elements. There are $q$ queries to process, and each query consists of four integers: $l$, $r$, $x$, and $y$.

For the subarray of $A$ ranging from index $l$ to $r$, you need to assign a sequence of integers for each subsequent element. The sequence should start from $x$ and increase by $y$. This means:
- $A[l]$ will be assigned the value of $x$.
- $A[l+1]$ will be assigned the value of $x + y$.
- $A[l+2]$ will be assigned the value of $x + 2y$.
- Continuing this pattern, $A[l+i]$ will be assigned the value of $x + i \cdot y$, where $i$ ranges from $0$ to $(r - l)$.

Find the sum of all integers in $A$ after processing all queries. Since the answer can be large, return it modulo $10^9+7$.

### Input Format
1. The first line contains an integer, $n$, denoting the number of elements in $A$.
2. Each line $i$ of the $n$ subsequent lines (where $0 \le i < n$) contains an integer describing $A[i]$.
3. The next line contains an integer, $q$, denoting the number of rows in queries.
4. Each line $i$ of the $q$ subsequent lines (where $0 \le i < q$) contains 4 space-separated integers, each describing the row `queries[i]`. The 4 space-separated integers denote the value of $l$, $r$, $x$, and $y$ for the $i$-th query.

### Constraints
- $1 \le n \le 10^5$
- $0 \le A[i] \le 10^9$
- $1 \le q \le 10^5$
- $0 \le queries[i][j] \le 10^5$

---

### Sample Test Cases

#### Sample Input 1
```text
5
5
5
0
3
0
5
0 2 1 2
0 1 6 5
2 3 8 0
2 4 9 6
3 4 8 9
```

#### Sample Output 1
```text
51
```

#### Explanation 1
Here, $n = 5$, $A = [5, 5, 0, 3, 0]$, $q = 5$, and `queries = [[0, 2, 1, 2], [0, 1, 6, 5], [2, 3, 8, 0], [2, 4, 9, 6], [3, 4, 8, 9]]`.

- **For query 1**: $l = 0, r = 2, x = 1, y = 2$.
  - $A[0] = 1$
  - $A[1] = 3$
  - $A[2] = 5$
  - Array becomes: $A = [1, 3, 5, 3, 0]$
- **For query 2**: $l = 0, r = 1, x = 6, y = 5$.
  - $A[0] = 6$
  - $A[1] = 11$
  - Array becomes: $A = [6, 11, 5, 3, 0]$
- **For query 3**: $l = 2, r = 3, x = 8, y = 0$.
  - $A[2] = 8$
  - $A[3] = 8$
  - Array becomes: $A = [6, 11, 8, 8, 0]$
- **For query 4**: $l = 2, r = 4, x = 9, y = 6$.
  - $A[2] = 9$
  - $A[3] = 15$
  - $A[4] = 21$
  - Array becomes: $A = [6, 11, 9, 15, 21]$
- **For query 5**: $l = 3, r = 4, x = 8, y = 9$.
  - $A[3] = 8$
  - $A[4] = 17$
  - Array becomes: $A = [6, 11, 9, 8, 17]$

Hence, the answer is $6 + 11 + 9 + 8 + 17 = 51$.

#### Sample Input 2
```text
5
3
9
2
5
4
5
1 2 6 3
1 2 2 8
1 2 5 5
1 3 1 8
1 2 2 9
```

#### Sample Output 2
```text
37
```

#### Explanation 2
Here, $n = 5$, $A = [3, 9, 2, 5, 4]$, $q = 5$.
- **For query 1**: $l = 1, r = 2, x = 6, y = 3$. Array becomes $A = [3, 6, 9, 5, 4]$.
- **For query 2**: $l = 1, r = 2, x = 2, y = 8$. Array becomes $A = [3, 2, 10, 5, 4]$.
- **For query 3**: $l = 1, r = 2, x = 5, y = 5$. Array becomes $A = [3, 5, 10, 5, 4]$.
- **For query 4**: $l = 1, r = 3, x = 1, y = 8$. Array becomes $A = [3, 1, 9, 17, 4]$.
- **For query 5**: $l = 1, r = 2, x = 2, y = 9$. Array becomes $A = [3, 2, 11, 17, 4]$.
Hence, the answer is $3 + 2 + 11 + 17 + 4 = 37$.

#### Sample Input 3
```text
5
0
1
0
0
1
5
1 2 7 7
0 1 3 6
1 1 1 1
3 4 9 1
2 3 1 0
```

#### Sample Output 3
```text
16
```

#### Explanation 3
Here, $n = 5$, $A = [0, 1, 0, 0, 1]$, $q = 5$.
- **For query 1**: $l = 1, r = 2, x = 7, y = 7$. Array becomes $A = [0, 7, 14, 0, 1]$.
- **For query 2**: $l = 0, r = 1, x = 3, y = 6$. Array becomes $A = [3, 9, 14, 0, 1]$.
- **For query 3**: $l = 1, r = 1, x = 1, y = 1$. Array becomes $A = [3, 1, 14, 0, 1]$.
- **For query 4**: $l = 3, r = 4, x = 9, y = 1$. Array becomes $A = [3, 1, 14, 9, 10]$.
- **For query 5**: $l = 2, r = 3, x = 1, y = 0$. Array becomes $A = [3, 1, 1, 1, 10]$.
Hence, the answer is $3 + 1 + 1 + 1 + 10 = 16$.

---

## Sample 2: Medium (Optimal Sum Minimization/Maximization)

### Problem Description
You are given three integers $X$, $Y$, and $Z$, and two arrays $A$ and $B$, both of length $N$. You are also given an integer `sum` which is initially equal to $0$.

You have to perform $N$ operations, and in each $i$-th operation, you must do only one of the following:
1. Subtract $B[i]$ from `sum`.
2. Decrease both $X$ and $Y$ by 1, then add $A[i] \cdot X \cdot Y \cdot Z$ to `sum`.
3. Decrease both $Y$ and $Z$ by 1, then add $A[i] \cdot X \cdot Y \cdot Z$ to `sum`.

However, after each operation, $X$, $Y$, and $Z$ must all remain greater than or equal to $0$.

Find the maximum `sum` you can obtain after performing all operations. Since the answer can be large, return it modulo $10^9+7$.

### Input Format
1. The first line contains an integer, $N$, denoting the number of operations.
2. The next line contains an integer, $X$.
3. The next line contains an integer, $Y$.
4. The next line contains an integer, $Z$.
5. Each line $i$ of the $N$ subsequent lines (where $1 \le i \le N$) contains an integer describing $A[i]$.
6. Each line $i$ of the $N$ subsequent lines (where $1 \le i \le N$) contains an integer describing $B[i]$.

### Constraints
- $1 \le N \le 10^3$
- $1 \le X \le 10^3$
- $1 \le Y \le 10^3$
- $1 \le Z \le 10^3$
- $1 \le A[i] \le 10^6$
- $1 \le B[i] \le 10^9$

---

### Sample Test Cases

#### Sample Input 1
```text
2
1
2
2
0
0
10
5
```

#### Sample Output 1
```text
0
```

#### Explanation 1
Here, $N = 2, X = 1, Y = 2, Z = 2$, $A = [0, 0]$, $B = [10, 5]$.

- **Operation 1**: Apply type 2 operation (decrease $X, Y$ by 1, add $A[1]\cdot X\cdot Y\cdot Z$ to `sum`).
  - $X = 0, Y = 1, Z = 2$
  - `sum` = `sum` + $0 \cdot 0 \cdot 1 \cdot 2 = 0$
- **Operation 2**: Apply type 3 operation (decrease $Y, Z$ by 1, add $A[2]\cdot X\cdot Y\cdot Z$ to `sum`).
  - $X = 0, Y = 0, Z = 1$
  - `sum` = `sum` + $0 \cdot 0 \cdot 0 \cdot 1 = 0$

Hence, the answer is $0$.

#### Sample Input 2
```text
2
10
11
11
1
10
10
0
```

#### Sample Output 2
```text
9990
```

#### Explanation 2
Here, $N = 2, X = 10, Y = 11, Z = 11$, $A = [1, 10]$, $B = [10, 0]$.

- **Operation 1**: Apply type 1 operation (subtract $B[1]$ from `sum`).
  - `sum` = $0 - 10 = -10$
- **Operation 2**: Apply type 3 operation (decrease $Y, Z$ by 1, add $A[2]\cdot X\cdot Y\cdot Z$ to `sum`).
  - $X = 10, Y = 10, Z = 10$
  - `sum` = $-10 + 10 \cdot (10 \cdot 10 \cdot 10 \cdot 10) = -10 + 10000 = 9990$

Hence, the answer is $9990$.

#### Sample Input 3
```text
3
3
3
3
1
2
3
1
2
3
```

#### Sample Output 3
```text
35
```

#### Explanation 3
Here, $N = 3, X = 3, Y = 3, Z = 3$, $A = [1, 2, 3]$, $B = [1, 2, 3]$.

- **Operation 1**: Apply type 1 operation. `sum` = $0 - 1 = -1$.
- **Operation 2**: Apply type 2 operation (decrease $X, Y$).
  - $X = 2, Y = 2, Z = 3$.
  - `sum` = $-1 + 2 \cdot (2 \cdot 2 \cdot 3) = -1 + 24 = 23$.
- **Operation 3**: Apply type 3 operation (decrease $Y, Z$).
  - $X = 2, Y = 1, Z = 2$.
  - `sum` = $23 + 3 \cdot (2 \cdot 1 \cdot 2) = 23 + 12 = 35$.

Hence, the answer is $35$.

---

## Sample 3: Hard (Tree Beautiful Subsets)

### Problem Description
You are given a tree with $n$ nodes rooted at node 1. You are also given an array `color` representing the color of each node in the tree.

A set of nodes is **beautiful** if it satisfies the following conditions:
- All nodes in the set have different colors.
- For any pair of nodes $(u, v)$ in the set, either $u$ is the ancestor of $v$ or $v$ is the ancestor of $u$ within the tree. (This implies that the set of nodes forms a subset of some path from the root to a leaf).

You're given $q$ queries where each query provides an integer $s$ representing a node in the tree.
The answer to each query is the maximum size of a beautiful set that can be formed by selecting nodes from the subtree rooted at node $s$.

Find the sum of answers to all queries. Since the answer can be large, return it modulo $10^9+7$.

### Input Format
1. The first line contains an integer, $n$, denoting the number of nodes in the tree.
2. The next $n$ lines each contain an integer representing the parent of the $i$-th node (1-indexed, parent of node 1 is 0).
3. The next $n$ lines each contain an integer representing the color of the $i$-th node.
4. The next line contains an integer, $q$, denoting the number of queries.
5. The next $q$ lines each contain an integer $s$ representing the query node.

### Constraints
- $1 \le n \le 10^3$
- $1 \le color[i] \le n$ (or $10^6$)
- $1 \le q \le 10^3$
- The parent of node 1 is 0.

---

### Sample Test Cases

#### Sample Input 1
```text
5
0
1
2
1
3
4
3
4
3
5
3
4
3
3
```

#### Sample Output 1
```text
5
```

#### Explanation 1
Here, $n = 5$.
- Parent array: `p = [0, 1, 2, 1, 3]` (parent of 1 is 0, parent of 2 is 1, parent of 3 is 2, parent of 4 is 1, parent of 5 is 3).
- Color array: `color = [4, 3, 4, 3, 5]`
- Queries: `queries = [4, 3, 3]`

- **For query 1**: $s = 4$. Subtree of 4 contains only node 4. We can select $\{4\}$, answer is 1.
- **For query 2**: $s = 3$. Subtree of 3 contains nodes $\{3, 5\}$. Node 3 has color 4, node 5 has color 5. They are ancestor/descendant, different colors. We can select $\{3, 5\}$, answer is 2.
- **For query 3**: $s = 3$. Subtree of 3 contains $\{3, 5\}$, answer is 2.

Hence, the answer is $1 + 2 + 2 = 5$.

#### Sample Input 2
```text
5
0
1
1
2
2
1
5
4
5
2
3
5
4
3
```

#### Sample Output 2
```text
3
```

#### Explanation 2
Here, $n = 5$, `p = [0, 1, 1, 2, 2]`, `color = [1, 5, 4, 5, 2]`, `queries = [5, 4, 3]`.
- **For query 1**: $s = 5$. Subtree of 5 is $\{5\}$, answer is 1.
- **For query 2**: $s = 4$. Subtree of 4 is $\{4\}$, answer is 1.
- **For query 3**: $s = 3$. Subtree of 3 is $\{3\}$, answer is 1.
Hence, the answer is $1 + 1 + 1 = 3$.

#### Sample Input 3
```text
5
0
1
1
1
3
5
5
5
1
5
4
2
4
5
1
```

#### Sample Output 3
```text
5
```

#### Explanation 3
Here, $n = 5$, `p = [0, 1, 1, 1, 3]`, `color = [5, 5, 5, 1, 5]`, `queries = [2, 4, 5, 1]`.
- **For query 1**: $s = 2$. Subtree of 2 is $\{2\}$, answer is 1.
- **For query 2**: $s = 4$. Subtree of 4 is $\{4\}$, answer is 1.
- **For query 3**: $s = 5$. Subtree of 5 is $\{5\}$, answer is 1.
- **For query 4**: $s = 1$. Subtree of 1 is the whole tree. We can choose path $1 \to 3 \to 5$ which has colors $\{5, 5, 5\}$ (max distinct is 1), or path $1 \to 4$ which has colors $\{5, 1\}$ (both distinct, size 2). Thus max beautiful set is $\{1, 4\}$ with size 2.
Hence, the answer is $1 + 1 + 1 + 2 = 5$.
