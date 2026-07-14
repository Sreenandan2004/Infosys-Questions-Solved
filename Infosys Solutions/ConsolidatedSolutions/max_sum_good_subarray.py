import sys

def solve():
    """
    Naive solution for Max Sum of Good Subarray.
    Checks all possible subarrays A[l..r] and computes distinct count.
    Time Complexity: O(N^2)
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    A = [int(x) for x in input_data[2:n+2]]
    
    ans = 0 # Empty subarray has sum 0
    
    # Iterate over all possible starting indices l
    for l in range(n):
        distinct = set()
        curr_sum = 0
        # Iterate over all possible ending indices r
        for r in range(l, n):
            distinct.add(A[r])
            curr_sum += A[r]
            
            # Subarray is good if the number of distinct elements is <= k
            if len(distinct) <= k:
                if curr_sum > ans:
                    ans = curr_sum
            else:
                # Once distinct count exceeds k, extending the subarray further
                # will only keep the distinct count > k. So we can break.
                break
                
    print(ans)

if __name__ == '__main__':
    solve()
