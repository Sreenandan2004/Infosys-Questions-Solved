import sys

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, idx, val):
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & (-idx)

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & (-idx)
        return res

def solve():
    """
    Distinct Frequency Pairs using Fenwick Tree.
    Time Complexity: O(N log N).
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    A = [int(x) for x in input_data[1:n+1]]
    
    # Precompute F_left and D_left
    # F_left[i] = frequency of A[i] in A[0..i]
    # D_left[i] = distinct elements in A[0..i] // 2
    f_left = [0] * n
    d_left = [0] * n
    freq_left = {}
    distinct_left = set()
    
    for i in range(n):
        val = A[i]
        freq_left[val] = freq_left.get(val, 0) + 1
        f_left[i] = freq_left[val]
        distinct_left.add(val)
        d_left[i] = len(distinct_left) // 2
        
    # Precompute F_right and D_right
    # F_right[j] = frequency of A[j] in A[j..n-1]
    # D_right[j] = distinct elements in A[j..n-1] // 2
    f_right = [0] * n
    d_right = [0] * n
    freq_right = {}
    distinct_right = set()
    
    for j in range(n - 1, -1, -1):
        val = A[j]
        freq_right[val] = freq_right.get(val, 0) + 1
        f_right[j] = freq_right[val]
        distinct_right.add(val)
        d_right[j] = len(distinct_right) // 2
        
    # Calculate the target values:
    # We want to count pairs (i, j) with i < j such that:
    # F_left[i] - D_left[i] <= D_right[j] - F_right[j]
    val_left = [f_left[i] - d_left[i] for i in range(n)]
    val_right = [d_right[j] - f_right[j] for j in range(n)]
    
    # Coordinate compression
    all_vals = sorted(list(set(val_left + val_right)))
    val_map = {v: idx + 1 for idx, v in enumerate(all_vals)}
    
    compressed_left = [val_map[x] for x in val_left]
    compressed_right = [val_map[x] for x in val_right]
    
    bit = FenwickTree(len(all_vals))
    ans = 0
    MOD = 10**9 + 7
    
    # We iterate j from 0 to n-1. Before processing j,
    # the Fenwick tree contains all compressed_left[i] for i < j.
    for j in range(n):
        # Query how many i < j have compressed_left[i] <= compressed_right[j]
        ans = (ans + bit.query(compressed_right[j])) % MOD
        
        # Add compressed_left[j] to the Fenwick Tree
        bit.add(compressed_left[j], 1)
        
    print(ans)

if __name__ == '__main__':
    solve()
