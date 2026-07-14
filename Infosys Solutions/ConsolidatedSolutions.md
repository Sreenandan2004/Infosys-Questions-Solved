# Consolidated Solutions for Remaining 16 Problems

Here is the summary of the approaches and complexity for each of the 16 remaining problems from the PDFs. The Python source files are located in the [ConsolidatedSolutions](file:///d:/Learn/Problems/ConsolidatedSolutions/) directory.

---

## PDF 1 Problems

### 1. Arithmetic Progression Range Query
- **File:** [arithmetic_progression_range_query.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/arithmetic_progression_range_query.py)
- **Explainer:** [arithmetic_progression_range_queryExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/arithmetic_progression_range_queryExplainer.md)
- **Approach:** We use a Segment Tree with lazy propagation of linear functions ($a \cdot i + b$). Precomputing the sum of indices $\sum_{i=L}^R i$ allows us to perform range assignments of APs and range sum queries in $O(\log N)$ time per query.
- **Complexity:** Time: $O((N + Q) \log N)$, Space: $O(N)$

### 2. Sum Maximization
- **File:** [sum_maximization.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/sum_maximization.py)
- **Explainer:** [sum_maximizationExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/sum_maximizationExplainer.md)
- **Approach:** Since $c_2$ (number of times we choose Op 2) and $c_3$ (number of times we choose Op 3) uniquely determine the levels of $X, Y, Z$, we use DP with state `dp[c2][c3]` representing the maximum sum. At each step, we transition using the three options.
- **Complexity:** Time: $O(N \cdot X \cdot Z)$ (which is at most $O(N^3)$), Space: $O(X \cdot Z)$

---

## PDF 2 Problems

### 3. Food Stamps
- **File:** [food_stamps.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/food_stamps.py)
- **Explainer:** [food_stampsExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/food_stampsExplainer.md)
- **Approach:** We use binary search to find the optimal threshold $X$ for the meals. For any $X$, the number of meals with value $\ge X$ is monotonic. Once we find the threshold, we sum the taste points of all meals with value $> X$ and fill up to $M$ meals with value $X$.
- **Complexity:** Time: $O(N \log (\max V))$, Space: $O(1)$

### 4. MSS with Swaps
- **File:** [mss_with_swaps.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/mss_with_swaps.py)
- **Explainer:** [mss_with_swapsExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/mss_with_swapsExplainer.md)
- **Approach:** For each of the $O(N^2)$ subarrays $A[l..r]$, we can swap at most $k$ smallest elements inside the subarray with $k$ largest elements outside. We sort both sets and greedily perform the swaps.
- **Complexity:** Time: $O(N^3 \log N)$, Space: $O(N)$

---

## PDF 3 Problems

### 5. Range AP Update & Sum Queries
- **File:** [ap_range_sum_query.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/ap_range_sum_query.py)
- **Explainer:** [ap_range_sum_queryExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/ap_range_sum_queryExplainer.md)
- **Approach:** This is identical to PDF 1 Sample 1 but requires querying the current value of $A[l]$ from the segment tree before doing the lazy AP assignment $val \cdot (i - l + 1)$.
- **Complexity:** Time: $O((N + Q) \log N)$, Space: $O(N)$

### 6. Max Sum of Good Subarray
- **File:** [max_sum_good_subarray.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/max_sum_good_subarray.py)
- **Explainer:** [max_sum_good_subarrayExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/max_sum_good_subarrayExplainer.md)
- **Approach:** We use a sliding window to find the valid left endpoint range $[L_r, r]$ containing at most $k$ distinct elements. We maintain the minimum prefix sum in the window using a monotonic queue.
- **Complexity:** Time: $O(N)$, Space: $O(N)$

### 7. Oil Tank Disturbances
- **File:** [minimize_disturbances.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/minimize_disturbances.py)
- **Explainer:** [minimize_disturbancesExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/minimize_disturbancesExplainer.md)
- **Approach:** The number of disturbances as a function of the initial oil $X$ is convex. We use ternary search to find the minimum value of disturbances, then binary search to find the smallest $X$ that achieves it.
- **Complexity:** Time: $O(N \log C)$, Space: $O(1)$

### 8. Army Reduction Game
- **File:** [ali_army_reduction.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/ali_army_reduction.py)
- **Explainer:** [ali_army_reductionExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/ali_army_reductionExplainer.md)
- **Approach:** We use memoized recursion to find the minimum moves. The number of states visited is bounded by $O(\log^2 N)$, which is tiny.
- **Complexity:** Time: $O(\log^2 N)$, Space: $O(\log^2 N)$

### 9. Grid Invasion
- **File:** [grid_invasion.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/grid_invasion.py)
- **Explainer:** [grid_invasionExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/grid_invasionExplainer.md)
- **Approach:** Multi-source BFS starting from all invaded cells `A` to count the time to visit all enemy cells `E`.
- **Complexity:** Time: $O(N \cdot M)$, Space: $O(N \cdot M)$

### 10. Graph Component Beauty
- **File:** [connected_component_beauty.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/connected_component_beauty.py)
- **Explainer:** [connected_component_beautyExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/connected_component_beautyExplainer.md)
- **Approach:** The beauty of a set of elements $S$ is $|S| - (\text{number of consecutive pairs } (x, x+1) \in S)$. We use a DSU with small-to-large set merging to maintain the set of elements and consecutive pairs.
- **Complexity:** Time: $O(N \log^2 N)$, Space: $O(N)$

### 11. BFS on Circular Jumps
- **File:** [circular_jumping.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/circular_jumping.py)
- **Explainer:** [circular_jumpingExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/circular_jumpingExplainer.md)
- **Approach:** Shortest path BFS on a circular array from $X$ to $Y$.
- **Complexity:** Time: $O(N)$, Space: $O(N)$

### 12. Great Chain Probability
- **File:** [great_chain_probability.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/great_chain_probability.py)
- **Explainer:** [great_chain_probabilityExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/great_chain_probabilityExplainer.md)
- **Approach:** The problem corresponds to a bounded random walk on a 1D grid between $0$ and $K$. We use Matrix Exponentiation on the $(K+1) \times (K+1)$ transition matrix to find the probability of staying inside the bounds.
- **Complexity:** Time: $O(K^3 \log N)$, Space: $O(K^2)$

### 13. Max Subarray XOR Sum
- **File:** [max_subarray_xor_sum.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/max_subarray_xor_sum.py)
- **Explainer:** [max_subarray_xor_sumExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/max_subarray_xor_sumExplainer.md)
- **Approach:** We use a suffix Linear Basis to find the transition points where the max XOR sum changes. For each step $i$, there are at most 18 transition points. We use a Segment Tree to query range maximums of $dp$ in $O(\log N)$ time.
- **Complexity:** Time: $O(N \cdot \log(\max A) \cdot \log N)$, Space: $O(N)$

### 14. Min K for Path Length
- **File:** [min_k_for_path_length.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/min_k_for_path_length.py)
- **Explainer:** [min_k_for_path_lengthExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/min_k_for_path_lengthExplainer.md)
- **Approach:** We binary search for $k$. For a fixed $k$, we find the longest path by sorting the permutation and querying the maximum of $dp$ in range $[idx - k, idx + k]$ using a Segment Tree.
- **Complexity:** Time: $O(N \log^2 N)$, Space: $O(N)$

### 15. Soldiers & Treasure Chests
- **File:** [soldiers_treasure_chests.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/soldiers_treasure_chests.py)
- **Explainer:** [soldiers_treasure_chestsExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/soldiers_treasure_chestsExplainer.md)
- **Approach:** We precompute a Sparse Table on `Bonus` for $O(1)$ range maximum queries. We search for the first multiple of $A[i]$ to the right in $O(\log N)$ average time, and query the maximum.
- **Complexity:** Time: $O(N \log N)$, Space: $O(N \log N)$

### 16. Distinct Frequency Pairs
- **File:** [distinct_frequency_pairs.py](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/distinct_frequency_pairs.py)
- **Explainer:** [distinct_frequency_pairsExplainer.md](file:///d:/Learn/Problems/Infosys%20Solutions/ConsolidatedSolutions/distinct_frequency_pairsExplainer.md)
- **Approach:** We rewrite the condition as $F_{left}[i] - D_{left}[i] \le D_{right}[j] - F_{right}[j]$ for $i < j$. We use coordinate compression and a Fenwick Tree to count the valid pairs.
- **Complexity:** Time: $O(N \log N)$, Space: $O(N)$
