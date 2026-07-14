import sys

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [-float('inf')] * (4 * n)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return -float('inf')
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return max(self.query(2 * node, start, mid, l, r), self.query(2 * node + 1, mid + 1, end, l, r))

def solve():
    """
    Max Subarray XOR Sum using DP and Suffix Linear Basis.
    Time Complexity: O(N * (log(maxA)^2 + log(maxA) * log N)).
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    A = [int(x) for x in input_data[2:n+2] ]
    
    dp = [0] * (n + 1)
    
    # Segment tree to query max of dp[0..j]
    tree = SegmentTree(n + 1)
    tree.update(1, 0, n, 0, 0)
    
    # basis[b] will store (val, idx)
    basis = [None] * 20
    
    for i in range(1, n + 1):
        val = A[i-1]
        
        # Insert (val, i-1) into suffix basis
        curr_val = val
        curr_idx = i - 1
        for b in range(19, -1, -1):
            if (curr_val >> b) & 1:
                if basis[b] is None:
                    basis[b] = (curr_val, curr_idx)
                    break
                else:
                    b_val, b_idx = basis[b]
                    if curr_idx > b_idx:
                        # Keep larger index in basis, swap and continue inserting the other
                        basis[b] = (curr_val, curr_idx)
                        curr_val = b_val
                        curr_idx = b_idx
                    else:
                        curr_val ^= b_val
                        
        # Collect and sort all active transition points
        active = []
        for b in range(20):
            if basis[b] is not None:
                active.append(basis[b])
        # Sort in descending order of index
        active.sort(key=lambda x: x[1], reverse=True)
        
        # Calculate DP transitions
        dp[i] = dp[i-1] # We can always match nothing (size 0) for the current element, wait,
        # but the constraint is each subarray has length >= K.
        # So we can transition from j <= i - K.
        if i >= k:
            dp[i] = tree.query(1, 0, n, 0, i - k)
            
        # We can also extend any valid suffix
        # Suffixes starting at j <= i - K
        # The transition points partition starting indices j into intervals
        # Let's iterate through the active transition points
        curr_basis = []
        last_idx = i - 1
        
        for val, idx in active:
            # For starting indices in (idx .. last_idx], the basis elements are those with index > idx.
            # So the active elements in basis are the ones we've collected so far in curr_basis.
            # We want to find max(dp[j] + max_xor(curr_basis)) for j in [idx + 1, last_idx + 1] and j <= i - k + 1
            # Note: since dp is 1-indexed, starting index j (0-indexed) corresponds to dp[j].
            # So j range is [idx + 1, last_idx + 1] (in terms of dp indices, wait:
            # subarray is A[j..i-1], which is of length i-j.
            # Since length >= K, we need i-j >= K -> j <= i-K.
            # So dp index j ranges from 0 to i-K.
            # Let's find the intersection of [idx + 1, last_idx + 1] and [0, i - K]
            left = idx
            right = min(last_idx, i - k)
            
            if left <= right:
                # Query max of dp[left..right]
                max_dp = tree.query(1, 0, n, left, right)
                if max_dp != -float('inf'):
                    # Compute max XOR
                    xor_basis = []
                    for v in curr_basis:
                        res = v
                        for b in xor_basis:
                            if (res ^ b) < res:
                                res ^= b
                        if res > 0:
                            xor_basis.append(res)
                            xor_basis.sort(reverse=True)
                            
                    max_xor = 0
                    for v in xor_basis:
                        if (max_xor ^ v) > max_xor:
                            max_xor ^= v
                            
                    dp[i] = max(dp[i], max_dp + max_xor)
                    
            curr_basis.append(val)
            last_idx = idx
            
        # Handle the last interval: [0, last_idx]
        left = 0
        right = min(last_idx, i - k)
        if left <= right:
            max_dp = tree.query(1, 0, n, left, right)
            if max_dp != -float('inf'):
                xor_basis = []
                for v in curr_basis:
                    res = v
                    for b in xor_basis:
                        if (res ^ b) < res:
                            res ^= b
                    if res > 0:
                        xor_basis.append(res)
                        xor_basis.sort(reverse=True)
                        
                max_xor = 0
                for v in xor_basis:
                    if (max_xor ^ v) > max_xor:
                        max_xor ^= v
                dp[i] = max(dp[i], max_dp + max_xor)
                
        # Update segment tree with dp[i]
        tree.update(1, 0, n, i, dp[i])
        
    print(dp[n])

if __name__ == '__main__':
    solve()
