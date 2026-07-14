import sys

MOD = 10**9 + 7

def multiply(A, B, size):
    C = [[0] * size for _ in range(size)]
    for i in range(size):
        for k in range(size):
            if A[i][k] == 0:
                continue
            for j in range(size):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def power(A, p, size):
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        res[i][i] = 1
    base = A
    while p > 0:
        if p & 1:
            res = multiply(res, base, size)
        base = multiply(base, base, size)
        p >>= 1
    return res

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    B = int(input_data[2])
    R = int(input_data[3])
    
    # Probability computation: p = B / 10^6, q = R / 10^6
    inv10_6 = pow(10**6, MOD - 2, MOD)
    p_prob = (B * inv10_6) % MOD
    q_prob = (R * inv10_6) % MOD
    
    # State space: 0, 1, ..., K (size is K+1)
    size = k + 1
    M = [[0] * size for _ in range(size)]
    
    # Transition probability:
    # State j transitions to j+1 (by choosing B) with prob p_prob
    # State j transitions to j-1 (by choosing R) with prob q_prob
    for j in range(size):
        if j + 1 < size:
            M[j+1][j] = p_prob
        if j - 1 >= 0:
            M[j-1][j] = q_prob
            
    # Compute M^N
    M_N = power(M, n, size)
    
    # Initial state is 100% at state 0: v = [1, 0, ..., 0]^T
    # Sum of probabilities after N steps is sum_{i=0}^K M_N[i][0]
    ans = 0
    for i in range(size):
        ans = (ans + M_N[i][0]) % MOD
        
    print(ans)

if __name__ == '__main__':
    solve()
