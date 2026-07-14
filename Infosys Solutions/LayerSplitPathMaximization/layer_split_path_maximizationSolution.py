import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(300000)

def solve():
    """
    Finds the maximum value of a layer-split simple path in the graph.
    Uses memoized DFS with visited set reset when jumping to higher layers.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    L = [0] * n
    V = [0] * n
    idx = 3
    for i in range(n):
        L[i] = int(input_data[idx])
        V[i] = int(input_data[idx+1])
        idx += 2
        
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        # Only traverse edges in non-decreasing order of layers
        if L[u] <= L[v]:
            adj[u].append(v)
        if L[v] <= L[u]:
            adj[v].append(u)
            
    # Memoization table: (u, frozen_set_of_visited_in_current_layer) -> max score from u
    memo = {}
    
    def get_max(u, visited):
        state = (u, visited)
        if state in memo:
            return memo[state]
            
        max_val = 0  # 0 represents stopping the path at node u
        
        for v in adj[u]:
            if L[v] == L[u]:
                if v not in visited:
                    # Transition within the same layer (no penalty)
                    # Add v to the current layer's visited set
                    new_visited = visited.union((v,))
                    val = V[v] + get_max(v, new_visited)
                    if val > max_val:
                        max_val = val
            elif L[v] > L[u]:
                # Transition to a higher layer (with penalty)
                # Reset visited set for the new layer to just {v}
                penalty = (L[v] - L[u]) ** 2
                val = V[v] - penalty + get_max(v, frozenset([v]))
                if val > max_val:
                    max_val = val
                    
        memo[state] = max_val
        return max_val

    # Find the maximum path starting at any node
    ans = -float('inf')
    for start in range(n):
        ans = max(ans, V[start] + get_max(start, frozenset([start])))
        
    print(ans)

if __name__ == '__main__':
    solve()
