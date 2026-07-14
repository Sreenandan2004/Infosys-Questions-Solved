import sys

def solve():
    """
    Naive solution for Arithmetic Progression Range Queries.
    Directly loops and updates the array for each query.
    Time Complexity: O(Q * N)
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    A = [int(x) for x in input_data[1:n+1]]
    q = int(input_data[n+1])
    
    idx = n + 2
    MOD = 10**9 + 7
    
    for _ in range(q):
        l = int(input_data[idx])
        r = int(input_data[idx+1])
        x = int(input_data[idx+2])
        y = int(input_data[idx+3])
        idx += 4
        
        # Naive update: directly assign values in the range
        for i in range(l, r + 1):
            A[i] = x + (i - l) * y
            
    print(sum(A) % MOD)

if __name__ == '__main__':
    solve()
