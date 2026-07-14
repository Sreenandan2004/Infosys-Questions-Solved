import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

def solve():
    """
    Finds the sum of answers to subtree intersection queries under different roots.
    Uses DFS entry/exit times and binary lifting.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    A = int(input_data[1])
    B = int(input_data[2])
    
    # Parent array is 1-indexed. P[i] is parent of i.
    # Root has parent 0. We find the root node.
    P = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    root = 1
    
    idx = 3
    for i in range(1, n + 1):
        p_val = int(input_data[idx])
        P[i] = p_val
        idx += 1
        if p_val == 0:
            root = i
        else:
            adj[p_val].append(i)
            adj[i].append(p_val)
            
    q = int(input_data[idx])
    col = int(input_data[idx+1])
    idx += 2
    
    # DFS to compute entry/exit times, depth, and binary lifting table
    LOGN = 18
    up = [[0] * (n + 1) for _ in range(LOGN)]
    depth = [0] * (n + 1)
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    timer = 0
    
    def dfs(u, p, d):
        nonlocal timer
        timer += 1
        tin[u] = timer
        depth[u] = d
        up[0][u] = p
        for i in range(1, LOGN):
            up[i][u] = up[i-1][up[i-1][u]]
            
        for v in adj[u]:
            if v != p:
                dfs(v, u, d + 1)
        tout[u] = timer
        
    dfs(root, 0, 0)
    
    def is_ancestor(u, v):
        # Returns True if u is ancestor of v in default tree
        return tin[u] <= tin[v] <= tout[u]
        
    def get_child_ancestor(u, v):
        # Finds the child of u that is an ancestor of v
        # v is in subtree of u, and v != u
        curr = v
        for i in range(LOGN - 1, -1, -1):
            parent = up[i][curr]
            if parent != 0 and depth[parent] > depth[u]:
                curr = parent
        return curr

    def get_intervals(u, r):
        # Returns list of [tin, tout] intervals representing subtree of u when rooted at r
        if u == r:
            return [[1, n]]
        if not is_ancestor(u, r):
            return [[tin[u], tout[u]]]
        # r is in default subtree of u, find child C of u that is ancestor of r
        c = get_child_ancestor(u, r)
        res = []
        if tin[c] > 1:
            res.append([1, tin[c] - 1])
        if tout[c] < n:
            res.append([tout[c] + 1, n])
        return res

    ans_sum = 0
    last_ans = 0
    MOD = 10**9 + 7
    
    for _ in range(q):
        u_raw = int(input_data[idx])
        v_raw = int(input_data[idx+1])
        idx += 2
        
        # Online decrypter
        u = (u_raw + last_ans) % n + 1
        v = (v_raw + last_ans) % n + 1
        
        int_A = get_intervals(u, A)
        int_B = get_intervals(v, B)
        
        # Intersect intervals and find length
        curr_ans = 0
        for l1, r1 in int_A:
            for l2, r2 in int_B:
                l_max = max(l1, l2)
                r_min = min(r1, r2)
                if l_max <= r_min:
                    curr_ans += r_min - l_max + 1
                    
        ans_sum = (ans_sum + curr_ans) % MOD
        last_ans = curr_ans
        
    print(ans_sum)

if __name__ == '__main__':
    solve()
