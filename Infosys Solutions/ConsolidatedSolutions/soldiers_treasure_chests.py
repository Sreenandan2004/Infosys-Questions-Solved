import sys

class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        self.log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1
            
        k = self.log_table[n] + 1
        self.st = [[0] * k for _ in range(n)]
        
        for i in range(n):
            self.st[i][0] = arr[i]
            
        for j in range(1, k):
            for i in range(n - (1 << j) + 1):
                self.st[i][j] = max(self.st[i][j-1], self.st[i + (1 << (j-1))][j-1])
                
    def query(self, l, r):
        j = self.log_table[r - l + 1]
        return max(self.st[l][j], self.st[r - (1 << j) + 1][j])

def solve():
    """
    Soldiers & Treasure Chests using Sparse Table and Multiples Search.
    Time Complexity: O(N log N).
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    A = [int(x) for x in input_data[1:n+1]]
    Bonus = [int(x) for x in input_data[n+1:2*n+1]]
    
    # Precompute Sparse Table on Bonus
    st = SparseTable(Bonus)
    
    # pos[x] stores the first index to the right containing value x
    max_val = n // 2
    pos = [float('inf')] * (max_val + 1)
    
    total_xp = 0
    
    # Process from right to left
    for i in range(n - 1, -1, -1):
        v = A[i]
        
        # Find the first index R > i containing a multiple of v
        # We check all multiples m = v, 2v, 3v ... <= max_val
        r_index = float('inf')
        for m in range(v, max_val + 1, v):
            if pos[m] < r_index:
                r_index = pos[m]
                
        # If R is found, query max bonus in [i, r_index]
        if r_index != float('inf'):
            max_bonus = st.query(i, r_index)
            total_xp += max_bonus
            
        # Update pos for v
        pos[v] = i
        
    print(total_xp)

if __name__ == '__main__':
    solve()
