import sys

def solve():
    """
    Finds the maximum expert number of a partition.
    Uses optimized DP with time complexity O(N * max(A)).
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    A = [int(x) for x in input_data[1:n+1]]
    
    max_val = 1002
    last_pos = [-1] * (max_val + 2)
    min_last = [-1] * (max_val + 2)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        val = A[i-1]
        if val <= max_val:
            last_pos[val] = i - 1
            
        min_last[0] = i - 1
        dp[i] = dp[i-1]
        
        # Optimize loop in Python by local variables
        curr_min = i - 1
        for m in range(1, max_val + 1):
            # min_last[m] = min(min_last[m-1], last_pos[m-1])
            prev_last = last_pos[m-1]
            if prev_last < curr_min:
                curr_min = prev_last
            
            if curr_min >= 0:
                # If we partition at curr_min, the MEX of A[curr_min..i-1] is at least m
                cost = dp[curr_min] + m
                if cost > dp[i]:
                    dp[i] = cost
            else:
                break
                
    print(dp[n])

if __name__ == '__main__':
    solve()
