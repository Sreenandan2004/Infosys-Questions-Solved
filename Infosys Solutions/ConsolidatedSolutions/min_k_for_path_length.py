import sys

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = max(self.tree[node], val)
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return max(self.query(2 * node, start, mid, l, r), self.query(2 * node + 1, mid + 1, end, l, r))

def is_possible(k, n, m, p):
    # Sort elements by permutation value to process in increasing order of p[i]
    # We store pairs (p[i], i)
    nodes = sorted([(p[i], i) for i in range(n)])
    
    # Segment tree over indices 0..n-1
    tree = SegmentTree(n)
    dp = [0] * n
    
    for val, idx in nodes:
        # Query max of dp[j] for j in [idx - k, idx + k]
        l = max(0, idx - k)
        r = min(n - 1, idx + k)
        max_prev = tree.query(1, 0, n - 1, l, r)
        dp[idx] = max_prev + 1
        if dp[idx] >= m:
            return True
        tree.update(1, 0, n - 1, idx, dp[idx])
        
    return False

def solve():
    """
    Min K for Path Length using Binary Search and Segment Tree.
    Time Complexity: O(N log^2 N).
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    p = [int(x) for x in input_data[2:n+2]]
    
    # Binary search for min k
    low = 0
    high = n - 1
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid, n, m, p):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == '__main__':
    solve()
