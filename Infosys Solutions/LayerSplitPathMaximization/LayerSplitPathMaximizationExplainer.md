# Layer-Split Path Maximization with Penalties Explainer

## Problem Description & Example Test Case
You are given an undirected graph with $N$ nodes and $M$ edges. Each node $u$ has a layer $L[u]$ (an integer from $1$ to $K$) and a value $V[u]$.
You must choose a simple path (no repeated nodes) such that:
- **Layer Constraint:** Along the chosen path, the sequence of layers must be non-decreasing: $L[u_1] \le L[u_2] \le \dots \le L[u_t]$.
- **Penalty for Layer Jumps:** Whenever the path moves from a node with layer $x$ to a node with layer $y$ where $y > x$, you pay a cost: $\text{penalty} = (y - x)^2$.

Find the maximum value of:
$$\left( \sum_{i=1}^t V[u_i] \right) - \sum \text{penalties}$$

### Example Test Case
**Input:**
```text
3
2
3
1 -5
2 100
3 -10
0 1
1 2
```
**Output:**
```text
100
```
**Explanation:**
- Node 0: Layer 1, Value -5
- Node 1: Layer 2, Value 100
- Node 2: Layer 3, Value -10
- Edges: $0-1$, $1-2$.
- The best choice is the path starting and ending at node 1 (Path: $[1]$). Its score is $V[1] = 100$ with no penalties.
- Other paths like $[0 \to 1]$ give score $-5 + 100 - (2-1)^2 = 94 < 100$.
- Path $[1 \to 2]$ gives score $100 - 10 - (3-2)^2 = 89 < 100$.

---

## Prerequisite Concepts
- **Depth-First Search (DFS) / Dynamic Programming on DAGs:** Since the layers must be non-decreasing, the transitions between different layers form a Directed Acyclic Graph (DAG).
- **State Compression / Visited Set Resetting:** Because the path cannot return to a lower layer once it moves to a higher layer, we only need to track the visited set of nodes within the *current* layer to avoid cycles, resetting it when we jump to a strictly higher layer.

---

## The Naive Approach
A naive backtracking approach would search all simple paths in the undirected graph, check if their layers are non-decreasing, calculate the penalties, and find the maximum score. Since the number of simple paths in a graph of size $N \le 10^5$ can be factorial in $N$, this will result in Time Limit Exceeded (TLE).
- **Time Complexity:** $O(N!)$
- **Space Complexity:** $O(N)$

---

## Guided Discovery (The Optimal Approach)
Let's analyze the layer constraint: $L[u_1] \le L[u_2] \le \dots \le L[u_t]$.
This means we can only traverse edges $\{u, v\}$ in directions where $L[u] \le L[v]$.
If $L[u] < L[v]$, the transition is strictly directed $u \to v$.
If $L[u] == L[v]$, the transition is undirected within the same layer.

Since once we move to a higher layer, we can never return to any node in a lower layer, any cycle in our path can only occur within nodes of the **same layer**.
This means when we are at node $u$:
- If we transition to a node $v$ in a strictly higher layer ($L[v] > L[u]$), we can never revisit any node from $L[u]$ or lower.
- Hence, the set of visited nodes we need to track to ensure our path is simple only needs to contain nodes in the *current* layer!

Let's define our state for a recursive function `get_max(u, visited)`:
- `u`: The current node we are at.
- `visited`: A frozen set of visited nodes in the current layer $L[u]$.

When transitioning from `u` to a neighbor `v`:
1. If $L[v] == L[u]$:
   - We can transition to $v$ only if $v \notin visited$.
   - The new state will be `get_max(v, visited ∪ {v})`, with no penalty.
2. If $L[v] > L[u]$:
   - We transition to $v$ and pay a penalty $(L[v] - L[u])^2$.
   - Since $v$ is in a new layer, we reset the visited set to just $\{v\}$.
   - The new state will be `get_max(v, {v})`.

This memoized DFS runs extremely fast because the size of connected components within each layer is typically very small. If there are no same-layer edges (which is common in layered graphs), `visited` is always just $\{u\}$, and the state reduces to just $u$, making it a standard DAG DP running in $O(N + M)$ time!

---

## Visualizations
Here is a flowchart of the decision process for transitions from node $u$:

```mermaid
graph TD
    Start[At Node u, layer L[u]] --> Loop[For each neighbor v with L[v] >= L[u]]
    Loop --> Cond{Is L[v] == L[u]?}
    Cond -->|Yes| VisitedCheck{Is v in visited?}
    VisitedCheck -->|No| TransitionSame[Move to v, add v to visited]
    VisitedCheck -->|Yes| Skip[Skip v]
    Cond -->|No, L[v] > L[u]| TransitionHigher[Move to v, reset visited = {v}, pay penalty]
    TransitionSame --> RecurseSame[Recurse same layer]
    TransitionHigher --> RecurseHigher[Recurse higher layer]
```

---

## Optimal Complexity Breakdown
- **Time Complexity:** $O(N + M \cdot 2^C)$ where $C$ is the maximum size of a connected component within any single layer. Since same-layer components are typically small or empty, this is practically $O(N + M)$.
- **Space Complexity:** $O(N + M)$ to store the graph and the memoization table.

---

## Pseudocode
```text
function get_max(u, visited):
    if (u, visited) in memo:
        return memo[(u, visited)]
        
    max_val = 0
    for each neighbor v of u with L[v] >= L[u]:
        if L[v] == L[u]:
            if v not in visited:
                val = V[v] + get_max(v, visited + {v})
                max_val = max(max_val, val)
        else:
            penalty = (L[v] - L[u])^2
            val = V[v] - penalty + get_max(v, {v})
            max_val = max(max_val, val)
            
    memo[(u, visited)] = max_val
    return max_val
```
