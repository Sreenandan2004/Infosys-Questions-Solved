import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

def solve():
    """
    Finds the maximum size of a beautiful set in subtrees.
    Computes max distinct colors on downward paths for each node using DFS,
    then aggregates subtree maximums.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # Parent array is 1-indexed. P[i] is parent of node i.
    # Color array is 1-indexed.
    P = [0] * (n + 1)
    color = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    
    idx = 1
    for i in range(1, n + 1):
        P[i] = int(input_data[idx])
        idx += 1
        if P[i] != 0:
            children[P[i]].append(i)
            
    for i in range(1, n + 1):
        color[i] = int(input_data[idx])
        idx += 1
        
    q = int(input_data[idx])
    idx += 1
    queries = []
    for _ in range(q):
        queries.append(int(input_data[idx]))
        idx += 1
        
    # Step 1: Compute dp[u] (max distinct colors on a downward path starting at u)
    dp = [0] * (n + 1)
    
    # We can use a standard backtracking DFS
    def dfs_distinct(u, current_set):
        c = color[u]
        already_present = c in current_set
        if not already_present:
            current_set.add(c)
            
        max_dist = len(current_set)
        for v in children[u]:
            val = dfs_distinct(v, current_set)
            if val > max_dist:
                max_dist = val
                
        if not already_present:
            current_set.remove(c)
            
        return max_dist

    for u in range(1, n + 1):
        dp[u] = dfs_distinct(u, set())
        
    # Step 2: Compute ans[s] (max of dp[v] in subtree of s)
    ans = [0] * (n + 1)
    
    def compute_ans(u):
        max_val = dp[u]
        for v in children[u]:
            val = compute_ans(v)
            if val > max_val:
                max_val = val
        ans[u] = max_val
        return max_val
        
    compute_ans(1)  # Root is always 1
    
    # Sum answers to all queries
    MOD = 10**9 + 7
    total_sum = 0
    for s in queries:
        total_sum = (total_sum + ans[s]) % MOD
        
    print(total_sum)

if __name__ == '__main__':
    solve()
