import sys

def solve():
    """
    Naive solution for AP Range Sum Query.
    Directly modifies elements and computes range sums using loops.
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
    ans_sum = 0
    
    for _ in range(q):
        type_q = int(input_data[idx])
        l = int(input_data[idx+1])
        r = int(input_data[idx+2])
        idx += 3
        
        if type_q == 1:
            # Query the current value of A[l]
            val = A[l]
            # Naive assignment in [l, r]
            for i in range(l, r + 1):
                A[i] = (i - l + 1) * val
        else:
            # Naive range sum query in [l, r]
            curr_sum = 0
            for i in range(l, r + 1):
                curr_sum = (curr_sum + A[i]) % MOD
            ans_sum = (ans_sum + curr_sum) % MOD
            
    print(ans_sum)

if __name__ == '__main__':
    solve()
