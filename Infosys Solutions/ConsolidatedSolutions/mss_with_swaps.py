import sys

def solve():
    """
    Maximum Subarray Sum with Swaps.
    Time Complexity: O(N^2 * k) using optimized heap/sorting for small-size swaps.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    a = [int(x) for x in input_data[2:n+2]]
    
    ans = -float('inf')
    
    # Iterate over all possible subarrays a[l..r]
    for l in range(n):
        inside = []
        for r in range(l, n):
            inside.append(a[r])
            
            # Elements outside the subarray are those in a[0..l-1] and a[r+1..n-1]
            outside = a[:l] + a[r+1:]
            
            # We want to swap at most k smallest inside elements with k largest outside elements
            # Sort inside in ascending, outside in descending
            sorted_in = sorted(inside)
            sorted_out = sorted(outside, reverse=True)
            
            curr_sum = sum(inside)
            # Perform up to k swaps
            for i in range(min(k, len(sorted_in), len(sorted_out))):
                if sorted_out[i] > sorted_in[i]:
                    curr_sum += sorted_out[i] - sorted_in[i]
                else:
                    break
                    
            if curr_sum > ans:
                ans = curr_sum
                
    print(ans)

if __name__ == '__main__':
    solve()
