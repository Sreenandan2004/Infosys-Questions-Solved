import sys

def solve():
    """
    Sum Maximization using DP.
    Transitions:
    Op 1: sum -= B[i]
    Op 2: X -= 1, Y -= 1, sum += A[i]*X*Y*Z
    Op 3: Y -= 1, Z -= 1, sum += A[i]*X*Y*Z
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    X = int(input_data[1])
    Y = int(input_data[2])
    Z = int(input_data[3])
    A = [int(x) for x in input_data[4:n+4]]
    B = [int(x) for x in input_data[n+4:2*n+4]]
    
    # DP table: dp[c2][c3] = max sum after processing operations
    # c2 is count of Op 2, c3 is count of Op 3
    # c2 <= X, c3 <= Z, c2 + c3 <= n
    dp = {}
    dp[(0, 0)] = 0
    
    for i in range(n):
        new_dp = {}
        for (c2, c3), val in dp.items():
            # Op 1: Subtract B[i] from sum
            if (c2, c3) not in new_dp or val - B[i] > new_dp[(c2, c3)]:
                new_dp[(c2, c3)] = val - B[i]
                
            # Op 2: Decrease X and Y by 1, add A[i]*X_curr*Y_curr*Z_curr
            x_curr = X - c2
            y_curr = Y - c2 - c3
            z_curr = Z - c3
            if x_curr - 1 >= 0 and y_curr - 1 >= 0:
                cost = val + A[i] * (x_curr - 1) * (y_curr - 1) * z_curr
                if (c2 + 1, c3) not in new_dp or cost > new_dp[(c2 + 1, c3)]:
                    new_dp[(c2 + 1, c3)] = cost
                    
            # Op 3: Decrease Y and Z by 1, add A[i]*X_curr*Y_curr*Z_curr
            if y_curr - 1 >= 0 and z_curr - 1 >= 0:
                cost = val + A[i] * x_curr * (y_curr - 1) * (z_curr - 1)
                if (c2, c3 + 1) not in new_dp or cost > new_dp[(c2, c3 + 1)]:
                    new_dp[(c2, c3 + 1)] = cost
        dp = new_dp
        
    print(max(dp.values()) % (10**9 + 7))

if __name__ == '__main__':
    solve()
